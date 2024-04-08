from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    quantity = models.BigIntegerField()
    category = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    admin_status = models.TextField(blank=True, null=True)
    is_deleted = models.TextField(blank=True, null=True)
    is_published = models.BooleanField()
    currency = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', null=False, blank=True)

    class Meta:
        db_table = 'product'
