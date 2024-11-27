from django.db import models
from brands.models import Brand, Country

class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    phone_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=False)
    country_made = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.phone_name
