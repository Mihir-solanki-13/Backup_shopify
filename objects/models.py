import uuid
from django.db import models
from django.utils import timezone

OBJECT_TYPES = [
        ('Product', 'product'),
        ('Order', 'order'),
        ('type3', 'Type 3'),
        # Add more choices as needed
    ]

class Store(models.Model):
    store_id = models.UUIDField(default=uuid.uuid4, editable=False)
    organization_name = models.CharField(max_length=100)
    store_url = models.URLField()

class Object(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    object_type = models.CharField(max_length=10, choices=OBJECT_TYPES)  # Specify choices
    data = models.JSONField()  # Field to store JSON data
    id = models.UUIDField(default=uuid.uuid4, editable=False)  # Default UUID
    backup_date = models.DateField(default=timezone.now().date())  # Current date/time

    def __str__(self):  # Correcting method name to __str__
        return str(self.data)[13:32]   
