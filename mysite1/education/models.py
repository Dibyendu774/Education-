from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser
# from .managers import UserManager
from django.contrib.auth.models import User


class user(models.Model):
    DoesNotExist = None
    session = None
    objects = None
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=10)
    password = models.CharField(max_length=400)
    email = models.EmailField(default=000)
    phone_number = models.CharField(max_length=15, default=000)
    otp = models.CharField(max_length=100)
    Field = models.CharField(max_length=30, default='000')


class Role(models.TextChoices):
    STUDENT = 'Student', 'Student'
    FACULTY = 'Faculty', 'Faculty'


class Student(models.Model):
    session = None
    objects = None
    sid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    userno = models.CharField(max_length=20)
    dob = models.DateField()
    Gender = models.CharField(max_length=6)
    Email = models.EmailField()
    Number = models.CharField(max_length=10)
    course = models.CharField(max_length=30, default=000)
    Category = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Faculty(models.Model):
    session = None
    objects = None
    sid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    userno = models.CharField(max_length=20)
    dob = models.DateField()
    Gender = models.CharField(max_length=6)
    Email = models.EmailField()
    Number = models.CharField(max_length=10)
    course = models.CharField(max_length=30, default=000)
    Category = models.CharField(max_length=20, choices=Role.choices, default=Role.FACULTY)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Cont(models.Model):
    session = None
    objects = None
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    PH = models.CharField(max_length=10)
    Message = models.CharField(max_length=500)


class Add_product(models.Model):
    session = None
    objects = None
    Name = models.CharField(max_length=500, default=000)
    New_price = models.CharField(max_length=5)
    Old_price = models.CharField(max_length=5)
    Photo = models.ImageField(upload_to='product/')
    Dec = models.CharField(max_length=1500)


class Payment(models.Model):
    session = None
    objects = None
    Card_Number = models.CharField(max_length=16)
    Expiry = models.CharField(max_length=5)
    Cvv = models.CharField(max_length=5)
    Card_Name = models.CharField(max_length=25)


class home_add(models.Model):
    session = None
    objects = None
    main_name = models.CharField(max_length=1000)
    home_price = models.CharField(max_length=1000)
    home_image = models.ImageField(upload_to='home_product/')
    h6_head = models.CharField(max_length=1000)
    down_heading = models.CharField(max_length=1000)


class Profile1(models.Model):
    session = None
    objects = None
    Vb = models.OneToOneField(User, on_delete=models.CASCADE)
    has_completed_registration = models.BooleanField(default=False)

    def __str__(self):
        return self.Vb.username


class Student_Register_Res(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    UserName = models.CharField(max_length=40)
    Email_id = models.EmailField()
    Password_id = models.CharField(max_length=30)
    Country_Code = models.CharField(max_length=7)
    Phone_number_id = models.CharField(max_length=12)

