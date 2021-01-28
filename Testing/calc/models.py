from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    des= models.CharField(max_length=100)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)