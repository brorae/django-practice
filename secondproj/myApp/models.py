from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()



class Customer(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    body = models.TextField()
    