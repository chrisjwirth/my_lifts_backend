from django.urls import path

from .views import (
    ExerciseTemplateList,
    ExerciseTemplateDetail,
    WorkoutList,
    WorkoutDetail,
    ExerciseList,
    ExerciseDetail,
    SetList,
    SetDetail,
)

urlpatterns = [
    path(
        "templates/exercise-templates/<int:template_id>/",
        ExerciseTemplateDetail.as_view(),
        name="exercise_template_detail",
    ),
    path(
        "templates/exercise-templates/",
        ExerciseTemplateList.as_view(),
        name="exercise_template_list",
    ),
    path(
        "workouts/<int:workout_id>/exercises/<int:exercise_id>/sets/<int:set_id>/",
        SetDetail.as_view(),
        name="set_detail",
    ),
    path(
        "workouts/<int:workout_id>/exercises/<int:exercise_id>/sets/",
        SetList.as_view(),
        name="set_list",
    ),
    path(
        "workouts/<int:workout_id>/exercises/<int:exercise_id>/",
        ExerciseDetail.as_view(),
        name="exercise_detail",
    ),
    path(
        "workouts/<int:workout_id>/exercises/",
        ExerciseList.as_view(),
        name="exercise_list",
    ),
    path("workouts/<int:workout_id>/", WorkoutDetail.as_view(), name="workout_detail"),
    path("workouts/", WorkoutList.as_view(), name="workout_list"),
]
