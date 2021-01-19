from django.db import models
from datetime import datetime
# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    item_image = models.ImageField(default="2.jpg", blank=True)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now())
