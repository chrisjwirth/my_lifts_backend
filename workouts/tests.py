from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.timezone import now

from .models import Workout, Exercise, Set


class WorkoutTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.date = now()

        cls.user = get_user_model().objects.create_user(
            username="Testuser",
            email="test@email.com",
            password="secret",
        )

        cls.workout = Workout.objects.create(
            user=cls.user,
            date=cls.date,
            name="Test workout",
            location="Test location",
        )

        cls.exercise = Exercise.objects.create(
            workout=cls.workout,
            name="Test exercise",
            variation="Test variation",
            description="Test description",
        )

        cls.set = Set.objects.create(
            exercise=cls.exercise,
            set_number=1,
            weight=225,
            reps=10,
            seconds_working=90,
            seconds_resting=180,
        )

    def test_workout_models(self):
        self.assertEqual(self.workout.user.username, "Testuser")
        self.assertEqual(self.workout.name, "Test workout")
        self.assertEqual(
            str(self.workout), self.date.strftime("%B %-d, %Y - %-I:%-M %p")
        )
        self.assertEqual(self.exercise.name, "Test exercise")
        self.assertEqual(str(self.exercise), f"{self.workout} | Test exercise")
        self.assertEqual(self.set.set_number, 1)
        self.assertEqual(str(self.set), f"{self.exercise} | Set 1")
