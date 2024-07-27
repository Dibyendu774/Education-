from django.core.mail import send_mail
from django.urls import path
from django.shortcuts import redirect, render
from .models import *
from . import settings

def choose(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Occupation = request.POST['Occupation']
        Email = request.POST['Email']
        Email1 = Main_Page_Website.objects.filter(Email=Email).exists()
        if Email1:
            Err1 = 'This Email Is Already Existed !! 🤦‍♂️'
            return render(request, 'select.html', context={'Error': Err1})

        else:
            send_mail(
                'Register',
                f'You Have Successfully Registered {Email}',
                settings.EMAIL_HOST_USER,
                [Email, ]
            )
            Saving = Main_Page_Website(Name=Name, Occupation=Occupation, Email=Email)
            Saving.save()
            Success = 'Your Form Has Been Submitted ❤❤'
            return render(request, 'select.html', context={'Success': Success})

    else:
        return render(request, 'select.html')