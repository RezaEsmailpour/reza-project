from django.db import models
from datetime import datetime
from chef.models import Chef

# Create your models here.
class News(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    what = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title
