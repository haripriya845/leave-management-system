from django.db import models
from django.utils import timezone

class student(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone= models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone= models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    



class Leave(models.Model):

    student = models.ForeignKey(student, on_delete=models.CASCADE)
    
    subject = models.CharField(max_length=100)
    content = models.TextField()
    date_applied = models.DateField(auto_now_add=True)
    time_applied = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


