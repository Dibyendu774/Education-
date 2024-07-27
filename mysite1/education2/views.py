from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from .models import *
from django.contrib.auth.hashers import check_password, make_password


def Student_home(req):
    return redirect(Student_register_res)


@never_cache
def Student_login(request):
    if request.method == 'POST':
        role = request.POST.get('Role')

        if role == 'Student':
            fn = request.POST['fn']
            ln = request.POST['ln']
            un = request.POST['un']
            DOBi = request.POST['dob']
            Gen = request.POST['gen']
            Em = request.POST['Em']
            Phone = request.POST['Ph']
            course = request.POST['Dv']
            Role1 = request.POST['Role']
            u2 = Student(fname=fn, lname=ln, userno=un, dob=DOBi, Gender=Gen, Email=Em, Number=Phone,
                         course=course, Category=Role1)
            u2.save()
            return render(request, 'index.html')
    else:
        return render(request, 'student2.html')

@never_cache
def Student_register_res(request):
    if request.method == 'POST':
        Student_First_Name = request.POST['First_Name']
        Student_Last_Name = request.POST['Last_Name']
        Student_UserName_Name1 = request.POST['User_Name']
        Student_Email_id_Name = request.POST['Email_id']
        Student_Password_Name = request.POST['Password_id']
        Student_Password_Name2 = request.POST['Password_id1']
        Student_Country_Code_Name = request.POST['Country_Code']
        Student_Phone_Number_Name = request.POST['Student_Phone_Number']
        Email_commpare = Student_Register_Res.objects.filter(Email_id=Student_Email_id_Name).exists()

        if Email_commpare:
            Err = 'This Email Is Already Exists'
            return render(request, 'student_login_res.html', context={'Error': Err})

        if Student_Password_Name == Student_Password_Name2:
            Hashed_password = make_password(Student_Password_Name)
            Student_save = Student_Register_Res(First_Name=Student_First_Name, Last_Name=Student_Last_Name,
                                                UserName=Student_UserName_Name1, Email_id=Student_Email_id_Name,
                                                Password_id=Hashed_password, Country_Code=Student_Country_Code_Name,
                                                Phone_number_id=Student_Phone_Number_Name)
            Student_save.save()
            return render(request, 'student.html')

    else:
        return render(request, 'student_login_res.html')


def Student_Main_Home(request):
    return render(request, 'App2/black.html')

def Course45(request):
    return render(request, 'course-details.html')


@never_cache
def Blog(request):
    return render(request, 'blog.html')


@never_cache
def Blog_details(request):
    return render(request, 'blog-details.html')


@never_cache
def About44(request):
    return render(request, 'about44.html')


@never_cache
def Teachers(request):
    return render(request, 'teachers.html')


@never_cache
def Teacher_deatils(request):
    return render(request, 'teacher-details.html')


def Contact2(request):
    return render(request, 'contact45.html')


def Main_student1(request):
    return render(request, 'index.html')
