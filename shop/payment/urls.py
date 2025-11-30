from django.urls import path
from .views import CreatePaymentIntentView, PaymentListAPIView,StripeWebhookView


app_name = "payment"

urlpatterns = [
    path("create-intent/", CreatePaymentIntentView.as_view(), name="create-intent"),
    path("payment-history/", PaymentListAPIView.as_view(), name="payment-history"),
    path("webhook/", StripeWebhookView.as_view(), name="webhook"),
]
