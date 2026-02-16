from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema
from .serializers import PaymentSerializer
from .models import Payment

@extend_schema(tags=['Payments'])
class PaymentCreateView(generics.ListCreateAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

@extend_schema(tags=['Payments'])
class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer