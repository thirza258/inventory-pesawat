from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    engine = models.CharField(max_length=255, null=True, choices=[("Jet", "Jet"), ("Propeller", "Propeller")])
    winglet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.description}"