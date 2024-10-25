from django.urls import path
from .views import (FoodTypeListApiView,
                    FoodTypeDetailApiView,
                    FoodListApiView,
                    FoodDetailApiView,
                    CommentDetailApiView,
                    CommentListApiView)

urlpatterns = [
    path('foodtypes/', FoodTypeListApiView.as_view(), name='foodtype-list'),
    path('foodtypes/<int:pk>/', FoodTypeDetailApiView.as_view(), name='foodtype-detail'),

    path('foods/', FoodListApiView.as_view(), name='food-list'),
    path('foods/<int:pk>/', FoodDetailApiView.as_view(), name='food-detail'),

    path('type/<int:color_id>/food/', FoodListApiView.as_view()),

    path('comments/', CommentListApiView.as_view(), name='comment-list'),
    path('comments/<int:pk>', CommentDetailApiView.as_view(), name='comment-detail')

    ]