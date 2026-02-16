from django.urls import path
from .views import RegisterView,LoginView, LogoutView
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/obtain/', TokenObtainPairView().as_view, name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView().as_view, name='token-refresh'),
    path('api/token/verify/', TokenVerifyView().as_view, name='token-verify'),
] 