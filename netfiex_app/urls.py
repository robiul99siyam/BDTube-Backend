from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
# create router object
router = DefaultRouter()
# Register
router.register('category', views.categoryViewsets)
router.register("content", views.ContentViewSet)
router.register("review",views.reviewViewsets)
# router.register("like",views.Like_Post_Viewsets)


urlpatterns = [
    path('api/', include(router.urls)),
    path('video/<int:id>/like',views.LikeViewset.as_view(),name='like-create'),
    path('start_watching/<int:content_id>/', views.start_watching, name='start_watching'),
    path('stop_watching/<int:watch_log_id>/', views.stop_watching, name='stop_watching'),
    path('visualize_watch_times/', views.visualize_watch_times, name='visualize_watch_times'),
]