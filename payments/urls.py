from django.urls import path
from .views import CreatePaymentView, PaymentDetailView

urlpatterns = [
    path('create/', CreatePaymentView.as_view(), name='create-payment'),
    path('<str:payment_id>/', PaymentDetailView.as_view(), name='payment-detail'),
]
