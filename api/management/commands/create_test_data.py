from django.core.management import BaseCommand

from api.models import FoodCategory, Food

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load custom data into the database'

    def handle(self, *args, **options):
        # Создание категорий ( для полной проверки работоспособности в 1 категории часть подруктов опубликована во 2 оба не опубликованы
        category1 = FoodCategory.objects.create(
            name_ru='Первая категория',
            name_en='First Category',
            name_ch='第一类别',
            order_id=1,
        )

        category2 = FoodCategory.objects.create(
            name_ru='Вторая категория',
            name_en='Second Category',
            name_ch='第二类别',
            order_id=2,
        )

        # Создание продуктов для первой категории
        food1 = Food.objects.create(
            category=category1,
            is_vegan=False,
            is_special=False,
            code=1111,
            internal_code=111,
            name_ru="Продукт 1",
            description_ru="Описание продукта 1",
            description_en="Product 1 description",
            description_ch="产品 1 描述",
            cost=10.99,
            is_publish=False,
        )

        food2 = Food.objects.create(
            category=category1,
            is_vegan=True,
            is_special=True,
            code=2222,
            internal_code=222,
            name_ru="Продукт 2",
            description_ru="Описание продукта 2",
            description_en="Product 2 description",
            description_ch="产品 2 描述",
            cost=20.99,
            is_publish=True,
        )

        # Создание продуктов для второй категории
        food3 = Food.objects.create(
            category=category2,
            is_vegan=True,
            is_special=False,
            code=3333,
            internal_code=333,
            name_ru="Продукт 3",
            description_ru="Описание продукта 3",
            description_en="Product 3 description",
            description_ch="产品 3 描述",
            cost=15.99,
            is_publish=False,
        )

        food4 = Food.objects.create(
            category=category2,
            is_vegan=False,
            is_special=True,
            code=4444,
            internal_code=444,
            name_ru="Продукт 4",
            description_ru="Описание продукта 4",
            description_en="Product 4 description",
            description_ch="产品 4 描述",
            cost=25.99,
            is_publish=False,
        )

        self.stdout.write(self.style.SUCCESS('Custom data loaded successfully!'))
