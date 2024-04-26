from django.db import models
from django.conf import settings
from catalogue.models import Catalogue

class Order(models.Model):
    DRAFT = 'draft'
    FINALIZED = 'finalized'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (FINALIZED, 'Finalized'),
        (CANCELLED, 'Cancelled'),
    ]

    id = models.UUIDField(primary_key=True)
    email = models.EmailField(max_length=60, unique=True)
    name = models.CharField(max_length=50, null=True)
    address = models.TextField()
    quantity = models.IntegerField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Catalogue, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)

    def finalize(self):
        self.order_status = self.FINALIZED
        self.save()

    def cancel(self):
        self.order_status = self.CANCELLED
        self.save()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = "order"
