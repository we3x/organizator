from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

#class UserSerializer(serializers.ModelSerializer)
#    class Meta:
#        model = User
#        fields = ('id','name','')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name','owner')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id',
                  'name',
                  'description',
                  'date',
                  'duration',
                  'owner',
                  'project',
                 )
