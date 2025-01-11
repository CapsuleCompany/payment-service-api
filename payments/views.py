from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe
from .models import Payment
from .serializers import PaymentSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            # Create a payment intent with Stripe
            intent = stripe.PaymentIntent.create(
                amount=int(float(data['amount']) * 100),  # Amount in cents
                currency=data.get('currency', 'usd'),
                description=data.get('description', ''),
            )

            # Save payment record in the database
            payment = Payment.objects.create(
                amount=data['amount'],
                currency=data.get('currency', 'usd'),
                description=data.get('description', ''),
                stripe_payment_id=intent['id'],
                status='pending'
            )

            return Response({
                'client_secret': intent['client_secret'],
                'payment': PaymentSerializer(payment).data
            }, status=status.HTTP_201_CREATED)

        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailView(APIView):
    def get(self, request, payment_id, *args, **kwargs):
        try:
            payment = Payment.objects.get(stripe_payment_id=payment_id)
            return Response(PaymentSerializer(payment).data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
