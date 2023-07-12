from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    ADMIN = 'ADMIN'
    USER = 'USER'
    SUPPLIER = 'SUPPLIER'
    
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (USER, 'user'),
        (SUPPLIER, 'supplier')
    )
    
    user_type = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    
    


