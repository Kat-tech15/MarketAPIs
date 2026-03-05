from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
import random


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer')
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='buyer')

    def __str__(self):
        return f"{self.username}"
    

class Message(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    is_repied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.email}
    
class EmailOTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    attempts =  models.IntegerField(default=5)

    def __str__(self):
        return f'OTP for {self.user.email} - {self.code}'
    
    @staticmethod
    def generate_code():
        return str(random.randit(100000, 999999))
    
    @staticmethod
    def expiry_time(minutes=5):
        return timezone.now() +timedelta(minutes=minutes)
    
    @classmethod
    def create_for_user(cls, user, minutes_valid=5):
        code =  cls.generate_code()
        expire_at = cls.expiry_time(minutes=minutes_valid)
        return cls.objects.create(user=user, code=code, expire_at=expire_at)
    
    def is_expired(self):
        return timezone.now() > self.expires_at