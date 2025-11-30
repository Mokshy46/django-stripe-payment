from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet,ProductViewSet,ProductsCategoryViewSet

app_name = "products"

router = DefaultRouter()
router.register(r"categories",ProductsCategoryViewSet)
router.register(r"",ProductViewSet)
router.register(r"order",OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
