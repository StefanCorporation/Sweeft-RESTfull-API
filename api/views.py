from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from users.models import User
from workout_system.models import WorkoutCategory, WorkoutExercise, PersonalWorkoutPlan,  GoalTracking
from api.serializers import (UserSerializer, WorkoutCategorySerializer, WorkoutExercisesSerializer, 
                                PersonalWorkoutPlansSerializer, GoalTrackingSerializer) 


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    

    # if user is admin he got's all list of users if user is authenticated only he got's
    # his data
    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            username = self.request.user
        return User.objects.filter(username=username)



class WorkoutCategoryViewSet(ModelViewSet):
    queryset = WorkoutCategory.objects.all()
    serializer_class = WorkoutCategorySerializer    

    # Can only read without token
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(WorkoutCategoryViewSet, self).get_permissions()




class WorkoutExercisesViewSet(ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExercisesSerializer

    # Can only read without token 
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(WorkoutExercisesViewSet, self).get_permissions()



class PersonalWorkoutPlansViewSet(ModelViewSet):
    queryset = PersonalWorkoutPlan.objects.all()
    serializer_class = PersonalWorkoutPlansSerializer
    permission_classes = [IsAuthenticated]


    # if user is admin he got's all list of users if user is authenticated only he got's
    # his data
    def get_queryset(self):
        if self.request.user.is_staff:
            return PersonalWorkoutPlan.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            user = self.request.user
        return PersonalWorkoutPlan.objects.filter(user=user)
    



class GoalTrackingViewSet(ModelViewSet):
    queryset = GoalTracking.objects.all()
    serializer_class = GoalTrackingSerializer  
    permission_classes = [IsAuthenticated]  


    # if user is admin he got's all list of users if user is authenticated only he got's
    # his data
    def get_queryset(self):
        if self.request.user.is_staff:
            return GoalTracking.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            user = self.request.user
        return GoalTracking.objects.filter(user=user)
    


class ProfileViewSet(ModelViewSet):
    queryset = PersonalWorkoutPlan.objects.all()
    serializer_class = PersonalWorkoutPlansSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        if self.request.user.is_staff:
            return PersonalWorkoutPlan.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            user = self.request.user
        return PersonalWorkoutPlan.objects.filter(user=user)