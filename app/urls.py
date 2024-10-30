from django.urls import path
from rest_framework import routers
from .views import (FoodApiViewSet,
                    FoodTypeApiViewSet,
                    CommentApiViewSet)

app_name = 'app'

router = routers.DefaultRouter()
router.register("foodtypes", FoodTypeApiViewSet)
router.register("food", FoodApiViewSet)
router.register("comments", CommentApiViewSet)


urlpatterns = router.urls