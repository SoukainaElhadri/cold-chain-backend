from django.shortcuts import render
from rest_framework import viewsets
from .models import Capteur, Mesure, Ticket, AuditLog
from .serializers import (
    CapteurSerializer,
    MesureSerializer,
    TicketSerializer,
    AuditLogSerializer
)

class CapteurViewSet(viewsets.ModelViewSet):
    queryset = Capteur.objects.all()
    serializer_class = CapteurSerializer


class MesureViewSet(viewsets.ModelViewSet):
    queryset = Mesure.objects.all().order_by('-date')
    serializer_class = MesureSerializer

    # 👇 ICI C'EST LE BON ENDROIT
    def perform_create(self, serializer):
        mesure = serializer.save()

        # Vérifier la température
        if mesure.temp < 2 or mesure.temp > 8:
            Ticket.objects.create(
                titre="Température hors limite",
                description=f"Température détectée : {mesure.temp} °C",
                statut="Ouvert"
            )
            print("📨 Notification envoyée au technicien")


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-date_creation')
    serializer_class = TicketSerializer


class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all().order_by('-date')
    serializer_class = AuditLogSerializer
