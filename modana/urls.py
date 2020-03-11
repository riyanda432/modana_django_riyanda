from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from student import views

urlpatterns = [
    path('student/', views.student_list, name='student'),
    path('student/<int:pk>', views.student_detail,name='students')
]

urlpatterns = format_suffix_patterns(urlpatterns)