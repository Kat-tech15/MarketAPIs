import stripe 
import requests
from django.conf import settings
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentService:
    """
    Handles payment creation and processing for multiple gateways.
    """

    @staticmethod
    def create_payment(payment: Payment, user_phone=None):
        """
        Initiate a payment depending on the gateway.
        - Stripe: return client_secret for fronted.
        - M-pesa: send STK push request.
        """

        if payment.gateway == 'stripe':
            return PaymentService._create_stripe_intent(payment)
        
        elif payment.gateway == 'mpesa':
            if not user_phone:
                raise ValueError("Phone number required for M-pesa payments")
            return PaymentService._create_mpesa_payment(payment, user_phone)
        else:
            raise ValueError(f"Unsupported payment gateway: {payment.gateway}") 

    @staticmethod
    def _create_stripe_intent(payment: Payment):
        """
        Creates a stripe PaymentIntent and returns client_secret.
        
        """

        intent = stripe.PaymentIntent.create(
            amount = int(payment.amount * 100), # Stripe uses cents
            currency = 'usd',
            metadata = {'order_id': payment.order.id} 
        )   
        # Update payment status object with pending status
        payment.status = 'pending'
        payment.save()

    @staticmethod
    def _create_mpesa_payment(payment: Payment, phone_number):
        """
        sends STK Push request to M-pesa Daraja API
        
        """
        url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

        headers = {
            'Authorization': f'Bearer {settings.MPESA_TOKEN}',
            'Content_type': 'application/json'
        }

        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": settings.MPESA_PASSWORD,
            "Timestamp": "20260214123045",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": payment.amount,
            "PartyA": phone_number,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhonNumber": phone_number,
            "CallBackURL": settings.MPESA_CALLBACK_URL,
            "AccountRefrence": f"Order {payment.order.id}",
            "TransactionDesc": "Market payment"
        }

        response = requests.post(url, headers=headers, json=payload)

        payment.status = 'pending'
        payment.save()

        return response.json()