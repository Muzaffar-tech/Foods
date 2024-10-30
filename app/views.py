from rest_framework import generics, filters
from .models import Food, FoodType, Comment
from .serializers import FoodSerializer, FoodTypeSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .throttles import FoodAnonThrottle, FoodUserThrottle, FoodTypeUserThrottle, FoodTypeAnonThrottle, CommentUserThrottle, CommentAnonThrottle

class FoodTypeApiViewSet(ModelViewSet):
    serializer_class = FoodTypeSerializer
    queryset = FoodType.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'name']
    search_fields = ['name']
    throttle_classes = [FoodTypeUserThrottle, FoodTypeAnonThrottle]


class FoodApiViewSet(ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'name']
    search_fields = ['name', 'composition']
    throttle_classes = [FoodUserThrottle, FoodAnonThrottle]

    def get_queryset(self):
        if self.kwargs.get("food_type_id", False):
            foods = Food.objects.filter(food_type_id=self.kwargs.get("color_id"))
        else:
            foods = Food.objects.all()
        return foods



class CommentApiViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'name']
    search_fields = ['text', 'food', 'author']
    throttle_classes = [CommentUserThrottle, CommentAnonThrottle]

