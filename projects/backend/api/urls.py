from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'ticket',TicketViewSet)
router.register(r'project',ProjectViewSet)

urlpatterns = [
    url(
            r'^v0/',
                include(
                            router.urls,
                        ),
            ),
        ]
