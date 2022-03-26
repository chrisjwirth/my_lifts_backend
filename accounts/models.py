from django.contrib.auth.models import AbstractUser
from django.db import models

from workouts.exercise_template_seed import exercise_template_seed_data
from workouts.models import ExerciseTemplate


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(CustomUser, self).save(*args, **kwargs)
        if created:
            for exercise in exercise_template_seed_data:
                ExerciseTemplate.objects.create(user=self, **exercise)
