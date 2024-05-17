from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from django.db.models import Count, Q, F
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import FoodCategory, Food
from api.serializers import FoodListSerializer


class FoodCategoryListAPIView(ListAPIView):
    def get(self, request):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()

        serialized_data = []
        for category in categories:
            published_foods = category.food.filter(is_publish=True)
            if published_foods.exists():
                serialized_category = {
                    'id': category.id,
                    'name_ru': category.name_ru,
                    'foods': FoodListSerializer(published_foods, many=True).data
                }
                serialized_data.append(serialized_category)

        return Response(serialized_data)
