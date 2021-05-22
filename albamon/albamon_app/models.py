from django.db import models

# Create your models here.

class Job(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    information = models.TextField()
    pay = models.PositiveIntegerField()
    work = models.TextField(max_length=100)
    applier = models.PositiveIntegerField()

    def __str__(self):
        return self.name
