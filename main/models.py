from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    engine = models.CharField(max_length=255, null=True, choices=[("Jet", "Jet"), ("Propeller", "Propeller")])
    winglet = models.BooleanField(default=False)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.description}"