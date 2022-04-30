from django.urls import path
from myapp import views

urlpatterns = [
    
    path('index', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('otp/',views.otp,name='otp'),
    path('', views.login, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.profile,name='profile'),
    path('profile_pic',views.profile_pic,name='profile_pic'),
    path('course/', views.course, name='course'),
    path('course_detail/', views.course_detail, name='course_detail'),
    path('about/', views.about, name='about'),
    path('teacher/', views.teacher, name='teacher'),
    path('contact/', views.contact, name='contact'),

    
]
