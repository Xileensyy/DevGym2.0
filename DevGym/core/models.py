from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    # Agrega cualquier campo adicional que necesites para tu usuario
    # Ejemplo: campo de perfil, fecha de nacimiento, etc.
    pass

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hour = models.DateTimeField()
    cupos_disponibles = models.PositiveIntegerField(default=2)
    # Agrega cualquier campo adicional que necesites

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.hour}"