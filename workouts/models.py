from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date


class ExerciseTemplate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    variation = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.variation:
            return f"{self.user} | {self.name} | {self.variation}"
        else:
            return f"{self.user} | {self.name}"


class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.date.strftime("%B %-d, %Y")


class Exercise(models.Model):
    workout = models.ForeignKey(
        Workout, related_name="exercises", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    variation = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.workout} | {self.name}"


class Set(models.Model):
    exercise = models.ForeignKey(
        Exercise, related_name="sets", on_delete=models.CASCADE
    )
    set_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.DecimalField(
        max_digits=5, decimal_places=1, validators=[MinValueValidator(Decimal(0.0))]
    )
    reps = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )
    seconds_working = models.PositiveSmallIntegerField(null=True, blank=True)
    seconds_resting = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.exercise} | Set {self.set_number}"
