from django.db import models

# Create your models here.

class URLs(models.Model):
    article = models.CharField(max_length=50)
    url = models.URLField(max_length=1000)

    def __str__(self):
        return f"{self.article} - {self.url}"





class PriceProduct(models.Model):
    URLs = models.ForeignKey(URLs, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.price}"


