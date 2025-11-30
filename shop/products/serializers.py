from .models import Products, User, Order, OrderItem, ProductsCategory
from rest_framework import serializers




class ProductCategoryReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsCategory
        fields = "__all__"


class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")

        # Handle products with no image
        if not obj.image:
            return None

        try:
            url = obj.image.url
        except ValueError:
            return None  # File missing or deleted

        if request:
            return request.build_absolute_uri(url)

        return url



class ProductWriteSerializer(serializers.ModelSerializer):

    category = ProductCategoryReadSerializer()
    

    class Meta:
        model = Products
        fields = (
            "name",
            "price",
            "category",
            "desc",
            "image",

        )


    def create(self, validated_data):
        category = validated_data.pop("category")
        instance = ProductsCategory.objects.get_or_create(**category)
        product = Products.objects.create(**validated_data, category=instance)
        return product

    def update(self, instance, validated_data):
        if "category" in validated_data:
            nested_serializer = self.fields["category"]
            nested_instance = instance.category
            nested_data = validated_data.pop("category")
            nested_serializer.update(nested_instance, nested_data)
      
        return super(ProductWriteSerializer, self).update(instance, validated_data)
    



class OrderItemsSerializer(serializers.ModelSerializer):

    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "order",
            "product",
            "quantity",
            "price",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("order",)




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
            