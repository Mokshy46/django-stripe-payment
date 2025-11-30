from django.shortcuts import render
from rest_framework.views import APIView
import stripe
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



stripe.api_key = settings.STRIPE_SECRET_KEY


class CreatePaymentIntentView(APIView):

    def post(self, request, *args, **kwargs):

        amount = request.data.get("amount")

        # Validate missing amount
        if amount is None:
            return Response({"error": "Amount is required"}, status=400)

        # Validate integer input
        try:
            amount = int(amount)
        except (ValueError, TypeError):
            return Response({"error": "Amount must be an integer"}, status=400)

        # Validate positive amount
        if amount <= 0:
            return Response({"error": "Amount must be greater than 0"}, status=400)

        try:
            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                metadata={
                    "user_id": request.user.id if request.user.is_authenticated else "guest"
                },
            )

            # Save payment in database
            Payment.objects.create(
                payment_intent_id=intent.id,
                amount=amount,
                status=Payment.PENDING,
            )

            return Response(
                {
                    "client_secret": intent.client_secret,
                    "payment_intent_id": intent.id,
                },
                status=201,
            )

        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=400)

        




@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(View):
    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

        try:
            # Verify signature
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError:
            # Invalid signature
            return HttpResponse(status=400)

        # Handle events
        if event["type"] == "payment_intent.succeeded":
            intent = event["data"]["object"]
            payment_intent_id = intent["id"]

            print("PAYMENT SUCCESS:", payment_intent_id)

            # Update Payment model
            try:
              payment = Payment.objects.get(payment_intent_id=payment_intent_id)
              payment.status = Payment.COMPLETED
              payment.save()
            except Payment.DoesNotExist:
              print("Payment record not found.")

        elif event["type"] == "payment_intent.payment_failed":
            intent = event["data"]["object"]
            payment_intent_id = intent["id"]

            print("PAYMENT FAILED:", payment_intent_id)

            # Update Payment model
            try:
              payment = Payment.objects.get(payment_intent_id=payment_intent_id)
              payment.status = Payment.FAILED
              payment.save()
            except Payment.DoesNotExist:
              print("Payment record not found.")

        # Add other events if needed

        return HttpResponse(status=200)


class PaymentListAPIView(APIView):
    def get(self,request):
        payments = Payment.objects.all().order_by("-created_at")
        serializer = PaymentSerializer(payments, many = True)
        return Response(serializer.data)


