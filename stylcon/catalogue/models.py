from django.db import models
from datetime import timezone
# Create your models here.

class Catalogue(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    createdat = models.DateTimeField(db_column='createdAt', default=timezone.now, blank=True, null=True)
    updatedat = models.DateTimeField(db_column='updatedAt', default=timezone.now, blank=True, null=True)
