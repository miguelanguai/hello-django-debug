from django.urls import path
from .views import RegisterView, LoginView, TestTokenView
from . import views

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('test_token', TestTokenView.as_view(), name='test_token'),
]
