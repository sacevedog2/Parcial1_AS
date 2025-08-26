from django.db import models

# Create your models here.

class Flight(models.Model):
    class FlightType(models.TextChoices):
        NACIONAL = 'N', 'Nacional'
        INTERNACIONAL = 'I', 'Internacional'

    name  = models.CharField(max_length=120)
    ftype = models.CharField(max_length=1, choices=FlightType.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.name}"
