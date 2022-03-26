from django.contrib import admin

from .models import ExerciseTemplate, Workout, Exercise, Set

admin.site.register(ExerciseTemplate)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Set)
