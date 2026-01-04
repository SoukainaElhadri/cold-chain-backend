from django.urls import path, include
from rest_framework import routers
from .views import CapteurViewSet, MesureViewSet, TicketViewSet, AuditLogViewSet

router = routers.DefaultRouter()
router.register(r'capteurs', CapteurViewSet)
router.register(r'mesures', MesureViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'audit', AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
