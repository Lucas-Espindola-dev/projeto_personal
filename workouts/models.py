from django.db import models


class Exercises(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    instructional_video = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    workout = models.ForeignKey


class Cardio(models.Model):
    name = models.CharField()
    time = models.IntegerField(blank=True, null=True)
    kcal = models.IntegerField(blank=True, null=True)
    instructional_video = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    workout = models.ForeignKey

