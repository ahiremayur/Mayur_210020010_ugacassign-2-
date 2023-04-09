from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length= 200)
    Roll_number = models.IntegerField()
    Department = models.CharField(max_length=50)
    hostel = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)