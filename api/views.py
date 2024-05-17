from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.models import FoodCategory
from api.serializers import FoodListSerializer


class FoodCategoryListAPIView(ListAPIView):
    serializer_class = FoodListSerializer
    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).distinct()
        return queryset
