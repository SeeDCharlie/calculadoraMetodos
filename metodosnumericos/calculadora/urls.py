from django.urls import path
<<<<<<< HEAD
from .views import index, suma_resta, calcSumRest
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
from .views import index, suma_resta, calcSumRest
=======
<<<<<<< HEAD
>>>>>>> 712101bfa61377331de83ef3eeba5a591aa707cb
>>>>>>> d4b8b3a8f75685fc87a1cb3a61f6c06bc06bd7bb
from .views import *

urlpatterns = [
    path('', index),
    path('/home', index,name="home"),
    path('grafica', grafica, name="grafica"),
    path('montecarlo', monteCarlo,name="montecarlo"),

    path('primerCorte', primerCorte, name="primerCorte"),
    path('segundoCorte', segundoCorte, name="segundoCorte"),
    path('tercerCorte', tercerCorte, name="tercerCorte"),
<<<<<<< HEAD
    path('suma_resta', suma_resta, name = 'suma_resta'),
]
=======
    path('suma_resta/', suma_resta, name = 'suma_resta'),

    path('calcSumRest/', calcSumRest, name ='calcSumRest'),
]
<<<<<<< HEAD
=======
=======
>>>>>>> 2f58eb675e00601073510361d0c9d645d1b7c7e3
>>>>>>> 712101bfa61377331de83ef3eeba5a591aa707cb
>>>>>>> d4b8b3a8f75685fc87a1cb3a61f6c06bc06bd7bb
