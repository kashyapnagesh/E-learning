import email
from email import message
from plistlib import UID
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange

# Create your views here.

def index(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'index.html',{'uid':uid})

def register(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = 'Email is already register'
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global temp
                temp = {
                    'fname':request.POST['fname'],
                    'lname':request.POST['lname'],
                    'email':request.POST['email'],
                    'mobile':request.POST['mobile'],
                    'password':request.POST['password'],
                }
                otp = randrange(1000,9999)
                subject = 'welcome to GFG world'
                message = f'Welcome to App {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'otp.html',{'otp':otp})
            else:
                return render(request,'register.html',{'msg':'Both passwords are not same'})
    return render(request,'register.html')

def otp(request):
    if request.method == "POST":
        if request.POST['otp'] == request.POST['uotp']:
            global temp
            User.objects.create(
                fname = temp['fname'],
                lname = temp['lname'],
                email = temp['email'],
                mobile = temp['mobile'],
                password = temp['password'],
            )
            return render(request,'register.html',{'msg':'Account Created'})
        return render(request,'otp.html',{'msg':'Invalid OTP','otp':request.POST['otp']})
    return render(request,'register.html')

def login(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'uid':uid})
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email=request.POST['email'])
                if request.POST['password'] == uid.password:
                    request.session['email'] = request.POST['email']
                    return redirect('index')
                return render(request,'login.html',{'msg':'Inncorrect password'})
            except:
                msg = 'Email is not register'
                return render(request,'login.html',{'msg':msg})
                
        return render(request,'login.html')

def logout(request):
    del request.session['email']
    return render(request,'login.html')

def change_password(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if request.POST['opassword'] == uid.password:
            if request.POST['password'] == request.POST['cpassword']:
                uid.password = request.POST['password']
                uid.save()                   # update into database
                return render(request,'change-password.html',{'msg':'Password Change successfully','uid':uid})
            return render(request,'change-password.html',{'msg':'New Passwords are not same','uid':uid})
        return render(request,'change-password.html',{'msg':'Old Password is incorrect','uid':uid})
    return render(request,'change-password.html',{'uid':uid})


def forgot(request):
    if request.method =="POST":
        try:
            uid = User.objects.get(email=request.POST['email'])
            Nagesh=uid.password
            subject = 'Your Password'
            message = f'Password: {Nagesh}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list)  
            return render(request,'forgot.html',{'msg':'Password sent successfully'})
        except:
            return render(request,'forgot.html',{'msg':'invalid email'})              
    else:  
                return render(request, 'forgot.html')   

def change_password(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if request.POST['opassword'] == uid.password:
            if request.POST['password'] == request.POST['cpassword']:
                uid.password = request.POST['password']
                uid.save()                   # update into database
                return render(request,'change-password.html',{'msg':'Password Change successfully','uid':uid})
            return render(request,'change-password.html',{'msg':'New Passwords are not same','uid':uid})
        return render(request,'change-password.html',{'msg':'Old Password is incorrect','uid':uid})
    return render(request,'change-password.html',{'uid':uid})


def profile(request):
    # return render(request,'profile.html')
    uid = User.objects.get(email=request.session['email'])

    if request.method == "GET":
        return render(request,'profile.html',{'uid':uid})
    else:
        # uid = User.objects.get(email=request.session['email'])
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.mobile = request.POST['mobile']
        uid.save()
    return render(request,'profile.html',{'msg':'Edit Profile Page Succcessfully','uid':uid})

def profile_pic(request):
    uid = User.objects.get(email=request.session['email'])
    uid.pic = request.FILES['pic']
    uid.save()
    return render(request,'profile.html',{'uid':uid})

def course(request):
    uid = User.objects.get(email=request.session['email'])
    course_info = Course.objects.all()
    return render(request,'course.html',{'uid':uid, 'courses':course_info})

def course_detail(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'course_detail.html',{'uid':uid})

def about(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'about.html',{'uid':uid})

def teacher(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'teacher.html',{'uid':uid})

def contact(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        
        Contact.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        subject = request.POST['subject'],
        message = request.POST['message'],
     )
        return render(request,'contact.html',{'msg':'query submitted'})
    return render(request,'contact.html',{'uid':uid})

   


        

