from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    prd_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Products_set')
    prd_name = models.CharField(max_length=100)
    prd_price = models.FloatField(blank=True, null=True)
    prd_seller = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.prd_name)

    class Meta:
        ordering = ['prd_price']
