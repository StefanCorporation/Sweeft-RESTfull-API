from django.contrib import admin

from workout_system.models import WorkoutCategory, WorkoutExercise, PersonalWorkoutPlan, GoalTracking


admin.site.register(WorkoutCategory)
admin.site.register(GoalTracking)


@admin.register(WorkoutExercise)
class WorkoutExercisesAdmin(admin.ModelAdmin):
    search_fields = ['exercise_name']
    list_filter = ['category']

@admin.register(PersonalWorkoutPlan)
class PersonalWorkoutPlansAdmin(admin.ModelAdmin):
    search_fields = ['user__username']