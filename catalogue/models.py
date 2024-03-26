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
        

class Catalogue(models.Model):
    """
    This is a catalogue model for products
    """
    productCode = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name