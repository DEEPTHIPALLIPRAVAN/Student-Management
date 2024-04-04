from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
class User(AbstractUser):
    usertype=models.CharField(max_length=50)

class Teacher(models.Model):
    Name=models.CharField(max_length=20,blank=False,null=True)
    Phone_Number=models.IntegerField(null=True,blank=False)
    ConfirmPassword=models.CharField(max_length=20,null=True,blank=False)
    Department=models.CharField(max_length=30,null=True,blank=False)
    Experience=models.IntegerField(null=True,blank=False)
    Age=models.IntegerField(null=True,blank=False)
    T_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Student(models.Model):
    Name=models.CharField(max_length=30,blank=False,null=True)
    DOB=models.DateField(null=True,blank=False)
    Conf_pswd=models.CharField(max_length=50,null=True,blank=False)
    MobileNumber=models.BigIntegerField(null=True,blank=False)
    Gender=models.CharField(max_length=10,null=True,blank=False)
    S_id=models.ForeignKey(User,on_delete=models.CASCADE)

  
        



