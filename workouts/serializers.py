from rest_framework import serializers

from .models import ExerciseTemplate, Workout, Exercise, Set


class ExerciseTemplateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = (
            "id",
            "user",
            "name",
            "variation",
            "description",
            "notes",
        )
        model = ExerciseTemplate


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "exercise",
            "set_number",
            "weight",
            "reps",
            "seconds_working",
            "seconds_resting",
        )
        read_only_fields = ("exercise",)
        model = Set


class ExerciseSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            "id",
            "workout",
            "name",
            "variation",
            "description",
            "notes",
            "sets",
        )
        read_only_fields = ("workout",)
        model = Exercise


class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            "id",
            "user",
            "date",
            "name",
            "location",
            "notes",
            "exercises",
        )
        model = Workout
