import uuid
from django.db import models
from django.utils import timezone

OBJECT_TYPES = [
        ('products', 'products'),
        ('orders', 'orders'), 
        ('themes', 'themes'),
        ('pages','pages'),
        ('custom_collections','custom_collections'), 
        ('smart_collections','smart_collections'),
        ('locations','locations'),
        ('policies','policies'),
        ('shipping_zones','shipping_zones'),
        ('customers','customers'),  
        ('blogs','blogs'),
        ('inventory_levels','inventory_levels'),
         ('saved_searches','saved_searches'), # graphql
         ('files','files'),  #graph ql
         
    ]

class Store(models.Model):
    store_id = models.UUIDField(default=uuid.uuid4, editable=False)
    organization_name = models.CharField(max_length=100)
    store_url = models.URLField()

class Object(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    object_type = models.CharField(max_length=50, choices=OBJECT_TYPES)  # Specify choices
    data = models.JSONField()  # Field to store JSON data
    uuid = models.UUIDField(default=uuid.uuid4)  # Default UUID
    backup_date = models.DateField(default=timezone.now().date())  # Current date/time

    def __str__(self):
        return f"{self.object_type}_{self.uuid}"  
    
# log of restore api

