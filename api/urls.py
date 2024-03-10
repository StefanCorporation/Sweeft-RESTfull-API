from django.urls import path, include

from api.views import (UserViewSet, WorkoutCategoryViewSet, WorkoutExercisesViewSet, 
                            PersonalWorkoutPlansViewSet, GoalTrackingViewSet)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'category', WorkoutCategoryViewSet)
router.register(r'exerciese', WorkoutExercisesViewSet)
router.register(r'personal-plans', PersonalWorkoutPlansViewSet)
router.register(r'goal-traking', GoalTrackingViewSet)


app_name = 'api'

urlpatterns = [
    path('api/v1/', include(router.urls)) #127.0.0.1:8000/api/v1/....
]
