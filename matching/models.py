from django.db import models
from datetime import datetime

class BaseModel(models.Model):
    class Meta:
        abstract = True

    createdAt = models.DateTimeField(
        default=datetime.now
    )
    modifiedAt = models.DateTimeField(
        default=datetime.now
    )

    batch_date = models.CharField(
        max_length=12
    )

class Companies(BaseModel, models.Model):
    name = models.CharField(
        max_length=100
    )
    address = models.CharField(
        max_length=100
    )
    def __str__(self):
        return self.name

class Side(BaseModel, models.Model):
    name = models.CharField(
        max_length=100
    )
    def __str__(self):
        return self.name    

class Seekers(BaseModel, models.Model):
    
    seeker = models.ForeignKey(
        "Companies",
        on_delete=models.CASCADE,
        related_name = "companies"
    )
    side = models.ForeignKey(
        "Side",
        on_delete=models.CASCADE,
        related_name = "sides"
    )
    def __str__(self):
        return str(self.id)