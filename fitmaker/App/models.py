from django.db import models

# Create your models here.
class Product(models.Model):
    username=models.CharField(max_length=244)
    password=models.CharField(max_length=244)
    name=models.CharField(max_length=244)
    phonenumber=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,null=True)
    def __str__(self):
        return f"{self.name}"
