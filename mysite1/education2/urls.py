from django.urls import path
from .views import *


urlpatterns = [
    path('', Student_home),
    path('Course45', Course45),
    path('student2', Student_login),
    path('student3', Student_Main_Home),
    path('Blog', Blog),
    path('Blog-details', Blog_details),
    path('About44', About44),
    path('Teachers', Teachers),
    path('Teacher-deatils', Teacher_deatils),
    path('Contact45', Contact2),
    path('Student', Main_student1),
    path('Student_login', Student_register_res)
]