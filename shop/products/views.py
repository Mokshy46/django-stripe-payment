from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Products,ProductsCategory,Order,OrderItem
from .serializers import ProductCategoryReadSerializer,ProductWriteSerializer,ProductReadSerializer,OrderItemsSerializer,OrderSerializer


class ProductsCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductsCategory.objects.all()
    serializer_class = ProductCategoryReadSerializer
    permission_classes = [permissions.AllowAny]



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update","partial_update", "destroy"):
            return ProductWriteSerializer
        
        return ProductReadSerializer
        
    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = (permissions.AllowAny,)

        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = (permissions.IsAdminUser,)

        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


