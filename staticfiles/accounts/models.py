from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer')
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='buyer')
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.role} - {self.username}"
    

class Message(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.email}