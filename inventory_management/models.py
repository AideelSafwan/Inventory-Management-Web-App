from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class InventoryManagement(models.Model):
    code = models.CharField(max_length=5)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)