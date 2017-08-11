from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'Ticket',TicketViewSet)
router.register(r'Project',ProjectViewSet)

urlpatterns = [
    url(
            r'^v0/',
                include(
                            router.urls,
                        ),
            ),
        ]
