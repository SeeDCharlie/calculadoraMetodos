from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('grafica', grafica, name="grafica"),
    path('montecarlo', monteCarlo,name="montecarlo"),

    path('primerCorte', primerCorte, name="primerCorte"),
    path('segundoCorte', segundoCorte, name="segundoCorte"),
    path('tercerCorte', tercerCorte, name="tercerCorte"),

]