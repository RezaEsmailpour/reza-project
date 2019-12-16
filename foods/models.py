from django.db import models
from datetime import datetime
from chef.models import Chef

# Create your models here.
class Food(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    time = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

