from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class reviewModel(models.Model):
    username=models.CharField(max_length=200)
    review=models.TextField()
    rating=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])