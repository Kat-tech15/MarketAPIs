from django.urls import path
from .views import PaymentCreateView, PaymentDetailView

urlpatterns = [
    path('create/', PaymentCreateView.as_view()),
    path('detail/<int:pk>/', PaymentDetailView.as_view()),
]