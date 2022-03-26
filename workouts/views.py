from django.shortcuts import get_object_or_404
from rest_framework import exceptions, generics, serializers

from .models import ExerciseTemplate, Workout, Exercise, Set
from .permissions import IsWorkoutUserOrReadOnly
from .serializers import (
    ExerciseTemplateSerializer,
    WorkoutSerializer,
    ExerciseSerializer,
    SetSerializer,
)


class ExerciseTemplateList(generics.ListCreateAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = ExerciseTemplateSerializer

    def get_queryset(self):
        return ExerciseTemplate.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data["user"] != self.request.user:
            raise exceptions.PermissionDenied()
        serializer.save()


class ExerciseTemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = ExerciseTemplateSerializer
    queryset = ExerciseTemplate.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["template_id"])
        self.check_object_permissions(self.request, obj)
        return obj


class WorkoutList(generics.ListCreateAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data["user"] != self.request.user:
            raise exceptions.PermissionDenied()
        serializer.save()


class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["workout_id"])
        self.check_object_permissions(self.request, obj)
        return obj


class ExerciseList(generics.ListCreateAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return Exercise.objects.filter(
            workout=self.kwargs["workout_id"], workout__user=self.request.user
        )

    def perform_create(self, serializer):
        workout = Workout.objects.filter(pk=self.kwargs["workout_id"]).first()
        if workout.user != self.request.user:
            raise exceptions.PermissionDenied()
        serializer.save(workout=workout)


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["exercise_id"])
        self.check_object_permissions(self.request, obj)
        return obj


class SetList(generics.ListCreateAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = SetSerializer

    def get_queryset(self):
        return Set.objects.filter(
            exercise=self.kwargs["exercise_id"],
            exercise__workout__user=self.request.user,
        )

    def perform_create(self, serializer):
        exercise = Exercise.objects.filter(pk=self.kwargs["exercise_id"]).first()
        if exercise.workout.user != self.request.user:
            raise exceptions.PermissionDenied()
        serializer.save(exercise=exercise)


class SetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsWorkoutUserOrReadOnly,)
    serializer_class = SetSerializer
    queryset = Set.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["set_id"])
        self.check_object_permissions(self.request, obj)
        return obj
