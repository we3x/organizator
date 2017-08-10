from models import *
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (id,name)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (id, 
                  name,
                  description,
                  date,
                  time,
                  project,
                 )