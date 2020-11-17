from django.urls import path
from .views import *

from .views import index, calcSumaMatriz
from .views import *


urlpatterns = [
    path('', index),
    path('home/', index,name="home"),
    path('grafica/', grafica, name="grafica"),
    path('montecarlo/', monteCarlo,name="montecarlo"),

    path('primerCorte/', primerCorte, name="primerCorte"),
    path('segundoCorte/', segundoCorte, name="segundoCorte"),
    path('tercerCorte/', tercerCorte, name="tercerCorte"),

    #url para el calculo de la suma y resta de matrices
    path('restaM/', calcRestaMatriz, name = 'calcRestaMatriz'),
    path('calcSumaMatriz/', calcSumaMatriz, name ='calcSumaMatriz'),

    #url

]
