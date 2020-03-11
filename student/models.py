from django.db import models

class Student(models.Model):
    firstname   = models.CharField(max_length=100,blank=True)
    lastname    = models.CharField(max_length=100, blank=True)
    phonenumber = models.IntegerField()
    email       = models.EmailField(max_length=254)
    password    = models.CharField(max_length=199)
    created     = models.DateTimeField(auto_now_add=True)


    class Meta:

        ordering = ['created']
