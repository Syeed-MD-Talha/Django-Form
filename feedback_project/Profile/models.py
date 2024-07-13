from django.db import models

# Create your models here.
class Document(models.Model):
    upload=models.FileField(upload_to='images/')