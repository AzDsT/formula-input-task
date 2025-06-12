from django.urls import path
from .views import suggestion_api, editor_page

urlpatterns = [
    path('', editor_page, name='editor'),
    path('suggestions/', suggestion_api, name='suggestions'),
]