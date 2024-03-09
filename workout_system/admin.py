from django.contrib import admin

from workout_system.models import WorkoutCategory, WorkoutExercises, PersonalWorkoutPlans, GoalTracking


admin.site.register(WorkoutCategory)
admin.site.register(GoalTracking)


@admin.register(WorkoutExercises)
class WorkoutExercisesAdmin(admin.ModelAdmin):
    search_fields = ['exerciese_name']
    list_filter = ['category']

@admin.register(PersonalWorkoutPlans)
class PersonalWorkoutPlansAdmin(admin.ModelAdmin):
    search_fields = ['user__username']