from django.shortcuts import render

from rest_framework import generics

from tasks.serializers import TaskSerializer
from tasks.models import Task

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
                
        return queryset
    
    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()