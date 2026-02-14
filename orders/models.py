from django.db import models
from accounts.models import CustomUser
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.quantity}"