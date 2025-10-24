from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('studentregister/', views.studentregister, name='studentregister'),
    path('user_studentlogin/', views.user_studentlogin, name='user_studentlogin'),
    path('studentdashboard/', views.studentdashboard, name='studentdashboard'),
    path('student_edit/', views.student_edit, name='student_edit'),
    path('studentlogout/', views.studentlogout, name='studentlogout'),
    path('student_profile/',views.student_profile,name='student_profile'),
    path('apply_leave/',views.apply_leave,name='apply_leave'),
    path('teacherlogin/', views.teacherlogin, name='teacherlogin'),
    path('teacherregister/', views.teacherregister, name='teacherregister'),
    path('user_teacherlogin/', views.user_teacherlogin, name='user_teacherlogin'),
    path('teacherdashboard/', views.teacherdashboard, name='teacherdashboard'),


]
