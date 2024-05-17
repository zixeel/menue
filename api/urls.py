from django.urls import path
from rest_framework.routers import SimpleRouter

from api.apps import ApiConfig
from api.views import FoodCategoryListAPIView

app_name = ApiConfig.name

urlpatterns = [
    path('v1/foods/', FoodCategoryListAPIView.as_view(), name='FoodCategoryList'),
]


