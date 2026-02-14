from django.urls import path
from .views import OrderCreateView, OrderDetailView

urlpatterns = [
    path('create/', OrderCreateView.as_view()),
    path('detail/<int:pk>/', OrderDetailView.as_view()),
]