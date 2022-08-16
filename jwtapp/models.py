from django.db import models

# Create your models here.
class Brand (models.Model):
    name = models.CharField(max_length=50)
    sku = models.IntegerField()
    category = models.CharField(max_length=50)

    
