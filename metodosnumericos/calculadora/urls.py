from django.urls import path
from .views import index, suma_resta, calcSumRest
urlpatterns = [
    path('', index),
    path('suma_resta/', suma_resta, name = 'suma_resta'),
    path('calcSumRest/', calcSumRest, name ='calcSumRest'),
]