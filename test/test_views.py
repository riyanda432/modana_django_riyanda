from student.models import Student
from django.urls import reverse
from django.test import TestCase, Client
import json 

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.valid_payload = {
            "firstname": "dddddsdffd",
            "lastname": "deeef",
            "phonenumber": 855,
            "email": "f2f@g.com",
            "password": "yandsfdfsfsdfdssfsd"
        }
        
    def test_student_GET(self):
        response = self.client.get(reverse('student'))
        self.assertEquals(response.status_code,200)

    def test_student_GETs(self):
        response = self.client.get(reverse('student'))
        self.assertNotEquals(response.status_code,400)

    def test_student_POST(self):
        response = self.client.post('/student/',{
            "firstname": "dddddsdffd",
            "lastname": "deeef",
            "phonenumber": 855,
            "email": "f2f@g.com",
            "password": "yandsfdfsfsdfdssfsd"
        })
        self.assertEquals(response.status_code,201) 
    
    def test_student_POSTs(self):
        response = self.client.post('/student/',{
            "firstname": "dddddsdffd",
            "lastname": "deeef",
            "phonenumber": 855,
            "email": "f2f@g.com",
            "password": "yandsfdfsfsdfdssfsd"
        })
        self.assertNotEquals(response.status_code,400) 
    
    def test_student_DELETE(self): 
        new_list = Student.objects.create(
            firstname = "dffdfddf",
            lastname = "fdfddffdfd",
            phonenumber = 855,
            email = "f2f@g.com",
            password = "fdfddfdf")
        url = reverse('students', kwargs={'pk': new_list.pk})
        response = self.client.delete(url)
        self.assertEquals(response.status_code,204) 

    def test_student_DELETEs(self):
        new_list = Student.objects.create(
            firstname = "dffdfddf",
            lastname = "fdfddffdfd",
            phonenumber = 855,
            email = "f2f@g.com",
            password = "fdfddfdf")
        url = reverse('students', kwargs={'pk': new_list.pk})
        response = self.client.delete(url)
        self.assertNotEquals(response.status_code,400) 

    def test_student_PUT(self):
        new_list = Student.objects.create(
            firstname = "dffdfddf",
            lastname = "fdfddffdfd",
            phonenumber = 855,
            email = "f2f@g.com",
            password = "fdfddfdf")
        response = self.client.put(
            reverse('students', kwargs={'pk': new_list.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_student_PUTs(self):
        new_list = Student.objects.create(
            firstname = "dffdfddf",
            lastname = "fdfddffdfd",
            phonenumber = 855,
            email = "f2f@g.com",
            password = "fdfddfdf")
        response = self.client.put(
            reverse('students', kwargs={'pk': new_list.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertNotEqual(response.status_code, 400)
