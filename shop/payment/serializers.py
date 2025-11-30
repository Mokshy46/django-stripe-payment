from rest_framework import serializers
from .models import Payment
from products.models import Order



class PaymentSerializer(serializers.ModelSerializer):

    buyer = serializers.CharField(source="order.user.username", read_only=True)

    class Meta:
        model = Payment
        fields = (
            "id",
            "buyer",
            "status",
            "payment_option",
            "order",
            "created_at",
            "updated_at",
        )

        read_only_fields = ("status",)
    


class PaymentOptionSerializer(serializers.ModelSerializer):

    buyer = serializers.CharField(source="order.user.username", read_only=True)

    class Meta:
        model = Payment
        fields = (
            "id",
            "buyer",
            "status",
            "payment_option",
            "order",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("status", "order")