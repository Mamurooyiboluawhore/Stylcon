from django.db import models
import datetime
# Create your models here.

class Catalogue(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    createdat = models.DateTimeField(db_column='createdAt', default=datetime.datetime.now, blank=True, null=True)
    updatedat = models.DateTimeField(db_column='updatedAt', default=datetime.datetime.now, blank=True, null=True)

    class meta:
        db_name = 'catalogue'
        