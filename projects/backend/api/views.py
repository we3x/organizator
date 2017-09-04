from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrNotShow
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.


class TicketViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,IsOwnerOrNotShow,)
    serializer_class = TicketSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(owner=user)

    def get_serializer_context(self):
        return {'request': self.request}

class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,IsOwnerOrNotShow,)
    serializer_class = ProjectSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user)

    def get_serializer_context(self):
        return {'request': self.request}
