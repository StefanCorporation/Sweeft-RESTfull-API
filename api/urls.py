from django.urls import path, include

from api.views import (UserViewSet, WorkoutCategoryViewSet, WorkoutExercisesViewSet, 
                            PersonalWorkoutPlansViewSet, GoalTrackingViewSet)
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'category', WorkoutCategoryViewSet)
router.register(r'exerciese', WorkoutExercisesViewSet)
router.register(r'personal-plans', PersonalWorkoutPlansViewSet)
router.register(r'goal-traking', GoalTrackingViewSet)


app_name = 'api'

urlpatterns = [
    path('api/v1/', include(router.urls)), #127.0.0.1:8000/api/v1/....
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
