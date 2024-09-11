from django.db import models


class Exercises(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    instructional_video = models.CharField(max_length=255)
    comments = models.TextField()
    workout = models.ManyToOneRel()


