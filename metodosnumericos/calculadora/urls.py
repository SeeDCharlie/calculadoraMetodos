from django.urls import path
<<<<<<< HEAD
from .views import *
urlpatterns = [
    path('', index),
    path('grafica', grafica, name="grafica"),
    path('montecarlo', monteCarlo,name="montecarlo"),

    path('primerCorte', primerCorte, name="primerCorte"),
    path('segundoCorte', segundoCorte, name="segundoCorte"),
    path('tercerCorte', tercerCorte, name="tercerCorte"),

=======
from .views import index, suma_resta
urlpatterns = [
    path('', index),
    path('suma_resta/', suma_resta, name = 'suma_resta'),
>>>>>>> 449fb59fac1e4eba580ca87159c245d3ea8cdf5b
]