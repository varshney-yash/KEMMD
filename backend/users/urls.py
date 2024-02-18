from django.urls import path
from .api.controllers import RegisterAPI

user_url_patterns = [
    path('register/', RegisterAPI.as_view(), name='register-customer'),
]
