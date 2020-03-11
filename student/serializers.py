from rest_framework import serializers
from student.models import Student
import cryptography
from cryptography.fernet import Fernet

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    firstname   = serializers.CharField(required=True, allow_blank=False)
    lastname    = serializers.CharField(required=True, allow_blank=False)
    phonenumber = serializers.IntegerField()
    email       = serializers.EmailField(max_length=254)
    password    = serializers.CharField(required=True, allow_blank=False)

    passwords = "m".encode()
    key = Fernet.generate_key() 
    f = Fernet(key)
    encrypted = f.encrypt(passwords)
    
    def create(self, validated_data):
       passwords = validated_data['password'].encode(),
       key = Fernet.generate_key(),
       f = Fernet(self.key),
       encrypted = self.f.encrypt(self.passwords)

       return Student.objects.create(  

            firstname = validated_data['firstname'],
            lastname = validated_data['lastname'],
            phonenumber = validated_data['phonenumber'],
            email = validated_data['email'],
            password = encrypted,
        )
        
    def update(self,instance, validated_data):

        passwords = validated_data.get('password',instance.password).encode(),
        key = Fernet.generate_key(),
        f = Fernet(self.key),
        encrypted = self.f.encrypt(self.passwords)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)
        instance.email = validated_data.get('email', instance.email)
        instance.password = encrypted
        instance.save()
        return instance

