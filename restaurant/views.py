from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from restaurant.serializers import *
from restaurant.models import Restaurant, Category, Subcategory, Dish
from restaurant.utils.filter_backends import CustomFilterBackend
from restaurant.utils import CategoryFilter
from restaurant.utils.permissions_v2 import IsTheUserWhoCreated


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.select_related(
        "restaurant",
        "user"
    )

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CategoryAllFieldsSerializer
        else:
            return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif (
                self.action == "update" or
                self.action == "destroy" or
                self.action == "partial_update"
        ):
            return [IsTheUserWhoCreated()]
        else:
            return super().get_permissions()


class SubcategoryViewSet(ModelViewSet):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.select_related(
        "user",
        "parent"
    )
    filterset_class = CategoryFilter
    filter_backends = [CustomFilterBackend]

    def retrieve(self, request, *args, **kwargs):
        qs = Dish.objects.select_related(
            "user",
            "category",
        ).prefetch_related(
            "ingredients"
        ).filter(
            category_id=kwargs.get("pk")
        )
        qs = CustomFilterBackend().filter_queryset(request, qs, self)
        serializer = DishSerializer(
            qs,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif (
                self.action == "update" or
                self.action == "destroy" or
                self.action == "partial_update"
        ):
            return [IsTheUserWhoCreated()]
        else:
            return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return SubcategoryAllFieldsSerializer
        else:
            return super().get_serializer_class()


class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.select_related(
        "user",
        "category"
    ).prefetch_related(
        "ingredients"
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif (
                self.action == "update" or
                self.action == "destroy" or
                self.action == "partial_update"
        ):
            return [IsTheUserWhoCreated()]
        else:
            return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return DishAllFieldsSerializer
        else:
            return super().get_serializer_class()


class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.select_related("user")

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return RestaurantAllFieldsSerializer
        else:
            return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif (
                self.action == "update" or
                self.action == "destroy" or
                self.action == "partial_update"
        ):
            return [IsTheUserWhoCreated()]
        else:
            return super().get_permissions()


class CreateIngredientViewSet(CreateModelMixin,
                              RetrieveModelMixin,
                              DestroyModelMixin,
                              GenericViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.select_related(
        "user"
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action == "destroy":
            return [IsTheUserWhoCreated()]
        else:
            return super().get_permissions()
