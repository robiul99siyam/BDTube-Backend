from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,generics,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework import generics,status
from rest_framework.views import APIView
from django.contrib.auth.models import User
import json
#this is a model pleace
from .models import categoryModel,contentModel,ReviewModel,Notification,Like

# this is a serializer pleace 

from .serializer import categorySerializer,contentSerializer,reviewSeriailzer,LikeSerilizer



class categoryViewsets(viewsets.ModelViewSet):
    queryset = categoryModel.objects.all()
    serializer_class = categorySerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = contentModel.objects.all()
    serializer_class = contentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print('Instance ',instance)
        if request.user.is_authenticated:
            instance.view_count.add(request.user)

        serializer = self.get_serializer(instance)

        
       
        return Response(serializer.data)
    
   
class reviewViewsets(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = reviewSeriailzer


class LikeViewset(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerilizer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)