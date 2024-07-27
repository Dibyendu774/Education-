from django.db import models

# Create your models here.

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
    Category = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.fname} {self.lname}'

class Student_Register_Res(models.Model):
    session = None
    objects = None
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    UserName = models.CharField(max_length=40)
    Email_id = models.EmailField()
    Password_id = models.CharField(max_length=400)
    Country_Code = models.CharField(max_length=7)
    Phone_number_id = models.CharField(max_length=12)
