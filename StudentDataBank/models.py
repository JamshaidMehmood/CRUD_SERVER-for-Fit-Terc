from django.db import models

# Create your models here.

class Exercise(models.Model):
    exercise_title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    reps = models.IntegerField()
    date = models.DateField()

    