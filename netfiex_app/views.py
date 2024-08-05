from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,generics,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework import generics,status
from rest_framework.views import APIView
from django.contrib.auth.models import User
import json
import matplotlib.pyplot as plt
import os
from django.conf import settings
#this is a model pleace
from .models import categoryModel,contentModel,ReviewModel,Notification,Like,WatchLog

# this is a serializer pleace 

from .serializer import categorySerializer,contentSerializer,reviewSeriailzer,LikeSerilizer

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import F


class categoryViewsets(viewsets.ModelViewSet):
    queryset = categoryModel.objects.all()
    serializer_class = categorySerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = contentModel.objects.all()
    serializer_class = contentSerializer

    def retrieve(self, request, *args, **kwargs):
        # contentCount = contentModel.objects.filter(id=kwargs['pk'])
        # contentCount.update(
        #     view =F('view') + 1,
        # )
        # return super().retrieve(request,args,kwargs)


        instance = self.get_object()
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
    print("serailizer : ",serializer_class)
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def start_watching(request, content_id):
    content = get_object_or_404(contentModel, id=content_id)
    watch_log = WatchLog.objects.create(user=request.user, content=content, start_time=timezone.now())
    return JsonResponse({'status': 'started', 'watch_log_id': watch_log.id})

def stop_watching(request, watch_log_id):
    watch_log = get_object_or_404(WatchLog, id=watch_log_id)
    watch_log.end_time = timezone.now()
    watch_log.save()
    return JsonResponse({'status': 'stopped', 'watch_duration': watch_log.watch_duration()})





def visualize_watch_times(request):
    watch_logs = WatchLog.objects.filter(user=request.user)
    durations = [log.watch_duration() for log in watch_logs if log.end_time]

    plt.figure(figsize=(10, 6))
    plt.hist(durations, bins=20, edgecolor='black')
    plt.title('Watch Time Distribution')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Frequency')

   
    media_dir = settings.MEDIA_ROOT
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)

  
    plot_path = os.path.join(media_dir, 'watch_times.png')
    plt.savefig(plot_path)
    plt.close()  

   
    plot_url = os.path.join(settings.MEDIA_URL, 'watch_times.png')
    context = {'plot_url': plot_url}
    return render(request, 'visualize_watch_times.html', context)
