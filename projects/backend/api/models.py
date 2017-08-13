from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(unique=True, max_length=20)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateField()
    duration = models.IntegerField()
    project = models.ForeignKey(Project)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name
