from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    workout = models.ForeignKey

    def __str__(self):
        return self.name


class Cardio(models.Model):
    name = models.CharField(max_length=255)
    time = models.IntegerField(blank=True, null=True)
    kcal = models.IntegerField(blank=True, null=True)
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    workout = models.ForeignKey

    def __str__(self):
        return self.name


class Stretching(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField()
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    workout = models.ForeignKey

    def __str__(self):
        return self.name


class Mobility(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    time = models.TimeField()
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    workout = models.ForeignKey

    def __str__(self):
        return self.name

