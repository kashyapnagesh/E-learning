from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=13)
    password = models.CharField(max_length=30)
    pic=models.FileField(upload_to='profile',default='avtar.png' ,null=True, blank=True )


    def __str__(self):
        return self.email

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.email

class Course(models.Model):

    title = models.CharField(max_length=50)
    tname = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    duration = models.FloatField(default=0)
    img = models.FileField(upload_to='courses',default='default-course.jpg')
    
    def __str__(self):
        return self.title

class Course_details(models.Model):

   pass

