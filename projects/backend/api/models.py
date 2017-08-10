from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(unique=True, max_length=20)
    
class Ticket(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateField()
    time = models.IntegerField()
    project = models.ForeignKey('Project')
    
    