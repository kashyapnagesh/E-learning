from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['fname','lname','id','email','pic']

@admin.register(Contact)
class adminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

@admin.register(Course)
class adminContact(admin.ModelAdmin):
    list_display = ['title','tname','date','duration']