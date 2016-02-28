from django.db import models
from django.utils import timezone

# Create your models here.

class record(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False)
    text = models.CharField(max_length=1024, null=False, blank=False)
    record_date = models.DateTimeField(null=False, default=timezone.now)
