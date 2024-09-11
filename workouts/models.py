from django.db import models


class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    exercises = models.ManyToManyField('Exercises', related_name='workouts')
    cardio = models.ManyToManyField('Cardio', related_name='workouts')
    stretchings = models.ManyToManyField('Stretchings', related_name='workouts')
    mobility = models.ManyToManyField('Mobility', related_name='workouts')

    def __str__(self):
        return self.name

    def total_exercises(self):
        return self.exercises.count()  # Call count() on the related manager

    def total_cardio(self):
        return self.cardio.count()

    def total_stretchings(self):
        return self.stretchings.count()

    def total_mobility(self):
        return self.mobility.count()

    def total_workout_items(self):
        return (self.total_exercises() +
                self.total_cardio() +
                self.total_stretchings() +
                self.total_mobility())


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Cardio(models.Model):
    name = models.CharField(max_length=255)
    time = models.IntegerField(blank=True, null=True)
    kcal = models.IntegerField(blank=True, null=True)
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Stretching(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField()
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Mobility(models.Model):
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    instructional_video = models.URLField(max_length=255)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

