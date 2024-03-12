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
    #category = serializers.StringRelatedField(source='category.category_name')

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'exercise_name', 'exerciese_description', 'category', 'created_at']



class PersonalWorkoutPlansSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    exercise = WorkoutExercisesSerializer()


    class Meta:
        model = PersonalWorkoutPlan
        fields = ['id', 'user', 'exercise', 'frequency_per_week', 
                  'sets', 'duration', 'distance', 'goals', 'created_at']
        
        


class GoalTrackingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    personal_exercise = PersonalWorkoutPlansSerializer()

    # for nested fields
    def update(self, instance, validated_data):
        instance.user_weight = validated_data.get('user_weight', instance.user_weight)
        instance.goals = validated_data.get('goals', instance.goals)
        instance.save()
        return instance

    class Meta:
        model = GoalTracking
        fields = ['user', 'user_weight', 'goals', 'personal_exercise']


