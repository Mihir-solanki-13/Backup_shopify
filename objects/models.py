from django.db import models
from django.utils import timezone

class MyModel(models.Model):
    json_data = models.JSONField()  # Field to store JSON data
    version = models.CharField(max_length=255)  # Character field
    created_at = models.DateTimeField(default=timezone.now)  # Current date/time

     