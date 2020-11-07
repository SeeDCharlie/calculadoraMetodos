from django.urls import path
from .views import index, suma_resta
urlpatterns = [
    path('', index),
    path('suma_resta/', suma_resta, name = 'suma_resta'),
]