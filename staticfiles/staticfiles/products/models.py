from django.db import models

class Product(models.Model):
    PRODCT_CHOICES = (
        ('crops', 'Crops'),
        ('livestock', 'Livestock'),
        ('house_items', 'House_items')
    )
    type =  models.CharField(max_length=30, choices=PRODCT_CHOICES, default='crops')
    name = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='product/images', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {price}"
    