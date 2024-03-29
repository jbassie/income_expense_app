from .views import RegistrationView, UserNameValidationView
from django.urls import path

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('validate-username', UserNameValidationView.as_view())
]
