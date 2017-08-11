from rest_framework import viewsets
from serializers import *
from models import *
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

# Create your views here.
class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer
    queryset = serializer_class.Meta.model.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = serializer_class.Meta.model.objects.all()