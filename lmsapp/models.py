from django.db import models

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
    