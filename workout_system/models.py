from django.db import models
from django.utils import timezone

from users.models import User


class WorkoutCategory(models.Model):
    category_name = models.CharField(max_length=35, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.category_name



class WorkoutExercise(models.Model):
    exercise_name = models.CharField(max_length=50, unique=True, blank=True)
    exerciese_description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(WorkoutCategory, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Exercise: {self.exercise_name} | WorkoutCategory: {self.category.category_name}"



class PersonalWorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, null=True)
    frequency_per_week = models.IntegerField(null=True)
    sets = models.IntegerField(null=True)
    duration = models.DurationField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    goals = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Personal Workout Plan for: {self.user.username} | Exercise: {self.exercise.exercise_name}"



class GoalTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_weight = models.FloatField(default=0.0, null=True)
    goals = models.TextField(null=True, blank=True)
    personal_exercise = models.ForeignKey(PersonalWorkoutPlan, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Personal Goal Tracking for: {self.user.username}"

    
