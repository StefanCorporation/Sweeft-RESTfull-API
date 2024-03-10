from rest_framework import serializers

from users.models import User
from workout_system.models import WorkoutCategory, WorkoutExercise, PersonalWorkoutPlan, GoalTracking


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']



class WorkoutCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkoutCategory
        fields = ['id', 'category_name', 'created_at']



class WorkoutExercisesSerializer(serializers.ModelSerializer):
    category = WorkoutCategorySerializer()

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'exercise_name', 'exerciese_description', 'category', 'created_at']



class PersonalWorkoutPlansSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    exercise = WorkoutExercisesSerializer()

    class Meta:
        model = PersonalWorkoutPlan
        fields = ['id', 'user', 'exercise', 'frequency_per_week', 
                  'sets', 'duration', 'distance', 'goals', 'created_at']



class GoalTrackingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    personal_exercise = PersonalWorkoutPlansSerializer()

    class Meta:
        model = GoalTracking
        fields = ['user', 'user_weight', 'goals', 'personal_exercise']


