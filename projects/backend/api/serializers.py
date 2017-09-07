from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class FilterByUser(serializers.PrimaryKeyRelatedField):
    # This filters Projects by User
    def get_queryset(self):
        user = self.context['request'].user.id
        return Project.objects.filter(owner=user)

class FilterOwners(serializers.PrimaryKeyRelatedField):
    #Filters Owners by user that is logged in
    def get_queryset(self):
        user = self.context['request'].user.id
        return User.objects.filter(id=user)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name','owner')

class TicketSerializer(serializers.ModelSerializer):

    project = FilterByUser(many=False)
    owner  = FilterOwners(many=False)

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
