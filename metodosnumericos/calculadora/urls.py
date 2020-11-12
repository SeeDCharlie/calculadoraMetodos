from django.urls import path
<<<<<<< HEAD

from .views import index, suma_resta, calcSumRest

from .views import *
=======
from .views import index, suma_resta, calcSumaMatriz
from .views import *

>>>>>>> 62d38cb2cfdab2fc11c82fa7e47c50aa1e974fc3
urlpatterns = [
    path('', index),
    path('home/', index,name="home"),
    path('grafica/', grafica, name="grafica"),
    path('montecarlo/', monteCarlo,name="montecarlo"),

<<<<<<< HEAD
    path('primerCorte', primerCorte, name="primerCorte"),
    path('segundoCorte', segundoCorte, name="segundoCorte"),
    path('tercerCorte', tercerCorte, name="tercerCorte"),
    path('suma_resta', suma_resta, name = 'suma_resta'),
    path('suma_resta/', suma_resta, name = 'suma_resta'),
    path('calcSumRest/', calcSumRest, name ='calcSumRest'),
=======
    path('primerCorte/', primerCorte, name="primerCorte"),
    path('segundoCorte/', segundoCorte, name="segundoCorte"),
    path('tercerCorte/', tercerCorte, name="tercerCorte"),

    #url para el calculo de la suma y resta de matrices
    path('suma_resta/', suma_resta, name = 'suma_resta'),
    path('restaM/', calcRestaMatriz, name = 'calcRestaMatriz'),
    path('calcSumaMatriz/', calcSumaMatriz, name ='calcSumaMatriz'),
>>>>>>> 62d38cb2cfdab2fc11c82fa7e47c50aa1e974fc3
]
