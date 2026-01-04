from django.db import models

# Create your models here.
class Capteur(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mesure(models.Model):
    capteur = models.ForeignKey(Capteur, on_delete=models.CASCADE)
    temp = models.FloatField()
    hum = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.capteur.name} - {self.temp}°C / {self.hum}%"

class Ticket(models.Model):
    STATUT_CHOICES = [
        ('Ouvert', 'Ouvert'),
        ('En cours', 'En cours'),
        ('Clos', 'Clos'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='Ouvert'
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre



class AuditLog(models.Model):
    action = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}: {self.action}"
