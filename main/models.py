from django.db import models

# Create your models here.
class Product(models.Model):
    Nomi = models.CharField(max_length=100, blank=True, null=True)
    Title = models.CharField(max_length=150, blank=True, null=True)
    Narxi = models.FloatField()
    Tavsif = models.TextField(blank=True, null=True)
    Rasm = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.Nomi
