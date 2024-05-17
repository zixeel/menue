from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.models import FoodCategory
from api.serializers import FoodListSerializer


class FoodCategoryListAPIView(ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.all()
