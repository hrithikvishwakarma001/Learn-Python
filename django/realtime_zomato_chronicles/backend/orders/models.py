from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name