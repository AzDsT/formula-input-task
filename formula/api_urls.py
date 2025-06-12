from django.urls import path
from .views import suggestion_api

urlpatterns = [
    path('suggestions/', suggestion_api, name='suggestions'),
]
