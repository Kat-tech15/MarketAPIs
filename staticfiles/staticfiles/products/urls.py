from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('list/', ProductListView.as_view()),
    path('detail/<int:pk>/', ProductDetailView.as_view()),
]