from django.shortcuts import render

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import User
from workout_system.models import WorkoutCategory, WorkoutExercise, PersonalWorkoutPlan,  GoalTracking
from api.serializers import (UserSerializer, WorkoutCategorySerializer, WorkoutExercisesSerializer, 
                                PersonalWorkoutPlansSerializer, GoalTrackingSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(UserViewSet, self).get_permissions()
    


class WorkoutCategoryViewSet(ModelViewSet):
    queryset = WorkoutCategory.objects.all()
    serializer_class = WorkoutCategorySerializer    


    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(WorkoutCategoryViewSet, self).get_permissions()




class WorkoutExercisesViewSet(ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExercisesSerializer  


    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(WorkoutExercisesViewSet, self).get_permissions()




class PersonalWorkoutPlansViewSet(ModelViewSet):
    queryset = PersonalWorkoutPlan.objects.all()
    serializer_class = PersonalWorkoutPlansSerializer  


    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(PersonalWorkoutPlansViewSet, self).get_permissions()




class GoalTrackingViewSet(ModelViewSet):
    queryset = GoalTracking.objects.all()
    serializer_class = GoalTrackingSerializer  


    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super(GoalTrackingViewSet, self).get_permissions()