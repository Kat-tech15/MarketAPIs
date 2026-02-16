from rest_framework import mixins, permissions, generics, status
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order

@extend_schema(tags=['Orders'])
class OrderCreateView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class =  OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)

@extend_schema(tags=['Orders'])
class OrderDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        self.retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)