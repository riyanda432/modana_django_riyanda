from django.test import SimpleTestCase
from django.urls import resolve,reverse
from student.views import student_detail,student_list

class TestUrls(SimpleTestCase):
    
    def test_list_urls(self):
        url = reverse('student')
        self.assertEquals(resolve(url).func,student_list)

    def test_list_urlsw(self):
        url = reverse('student',args=[str(1)])
        self.assertNotEquals(resolve(url).func,student_detail)

