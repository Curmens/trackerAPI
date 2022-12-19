from django.db import models
from apps.pets.models import Pet

# Create your models here.
class Store(models.Model):
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shipDate = models.DateTimeField()
    status = models.CharField(max_length=50)
    complete = models.BooleanField()

    def __str__(self):
        return self.name