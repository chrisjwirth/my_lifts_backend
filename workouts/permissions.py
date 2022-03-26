from rest_framework import permissions

from .models import Workout


class IsWorkoutUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):
            return obj.user == request.user
        elif hasattr(obj, "workout"):
            return obj.workout.user == request.user
        elif hasattr(obj, "exercise"):
            return obj.exercise.workout.user == request.user
        return False
