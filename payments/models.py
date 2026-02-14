from django.db import models
from orders.models import Order
from accounts.models import CustomUser

class Payment(models.Model):
    GATEWAY_CHOICES=(
        ('stripe', 'Stripe'),
        ('mpesa', 'Mpesa')
    )
    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('approved', 'Approved')
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    gateway = models.CharField(max_length=10, choices=GATEWAY_CHOICES, default='stripe')
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='pending')
    transaction_id = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.id} - {self.status}"
