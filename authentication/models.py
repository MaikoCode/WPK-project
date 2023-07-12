from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    # On a par defaut certains champs comme username, password etc...
    
    ADMIN = 'ADMIN'
    USER = 'USER'
    SUPPLIER = 'SUPPLIER'
    
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (USER, 'user'),
        (SUPPLIER, 'supplier')
    )
    
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    
    
    


