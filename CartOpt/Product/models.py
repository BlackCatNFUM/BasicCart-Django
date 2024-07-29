from django.db import models


class Product(models.Model):
    title = models.CharField(
        max_length=250,
        null=False
    )
    price = models.PositiveBigIntegerField(default=0)

    
    def __str__(self):
        return f"{self.title} : {self.price}"