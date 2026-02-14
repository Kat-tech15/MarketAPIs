from rest_framework import generics, permissions
from .serializers import PaymentSerializer
from .models import Payment

class PaymentCreateView(generics.ListCreateAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer