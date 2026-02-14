from django.db import models
from accounts.models import CustomUser

class Product(models.Model):
    PRODUCT_CHOICES = (
        ('crops', 'Crops'),
        ('livestock', 'Livestock'),
        ('house_items', 'House_items')
    )
    type =  models.CharField(max_length=30, choices=PRODUCT_CHOICES, default='crops')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='product/images', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    