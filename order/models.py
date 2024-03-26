from django.db import models
from django.conf import settings


# Create your models here.
class Order(models.Model):
    """
        Order model for creating order table
    """
    id = models.UUIDField(primary_key=True)
    email = models.EmailField(max_length=60, unique=True)
    name = models.CharField(max_length=50, null=True)
    address = models.TextField()
    quantity = models.IntegerField()
    city = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=20)
    country = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    product = models.ForeignKey('catalogue.Catalogue', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class meta:
        '''
            metadata for the Order model
        '''
        db_name = "order"

        from django.db import models
