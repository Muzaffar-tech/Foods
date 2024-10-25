from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework import status, mixins
from .models import Food, FoodType, Comment
from .serializers import FoodSerializer, FoodTypeSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

class FoodTypeListApiView(generics.ListCreateAPIView):
    serializer_class = FoodTypeSerializer
    queryset = FoodType.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'name']
    search_fields = ['name']


class FoodListApiView(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'name']
    search_fields = ['name', 'composition']

    def get_queryset(self):
        if self.kwargs.get("food_type_id", False):
            foods = Food.objects.filter(food_type_id=self.kwargs.get("color_id"))
        else:
            foods = Food.objects.all()
        return foods





class CommentListApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['pk', 'name']
    search_fields = ['text', 'food', 'author']


class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class FoodTypeDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticated]

class FoodDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
