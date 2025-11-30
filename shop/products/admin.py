from django.contrib import admin
from .models import Products,ProductsCategory,Order,OrderItem


admin.site.register(Products)
admin.site.register(ProductsCategory)
admin.site.register(Order)
admin.site.register(OrderItem)

