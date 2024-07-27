from django.shortcuts import render, redirect
from .models import Admin
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from education.models import *


def Admin1(request):
    if request.method == 'POST':
        username = request.POST['Em']
        password23 = request.POST['Pw']

        try:
            print('xyz')
            records1 = Admin.objects.filter(Email=username).exists()
            if records1:
                if username == 'dilipkarmakar1978@gmail.com':
                    print('adr')
                    return redirect(Main_Admin)
                else:
                    return render(request, 'home.html')

        except User.DoesNotExist:
            Err = 'You Are Not A Administer !! '
            return render(request, 'App3/admin2.html', context={'Error': Err})
    else:
        return render(request, 'App3/admin2.html')

def Revenue(request):
    return render(request, 'App3/rev.html')


def Main_Admin(request):
    User3 = Student.objects.all().count()
    records = Student.objects.all()
    SW = Student.objects.filter(course='Application Developer').count()
    SDD = Student.objects.filter(course='Software Developer').count()
    STD = Student.objects.filter(course='Website Design').count()
    vb = user.objects.all().count()
    recordsn = user.objects.all()
    Faculty1 = Faculty.objects.all()
    Faculty12 = Faculty.objects.all().count()
    # print(no)
    # print(record)
    return render(request, 'App3/admin.html',
                  context={'std': records, 'Users1': User3, 'sv': SW, 'XYZ': SDD, 'ABC': STD, 'all': vb,
                           'ann': recordsn, 'Faculty': Faculty1, 'FacultyAs': Faculty12})



