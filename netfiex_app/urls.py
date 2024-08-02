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
   
]