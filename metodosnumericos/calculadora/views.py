from django.shortcuts import render
from calculadora.motores import SumaResta
# Create your views here.


def index(request):

    return render(request,'calculadora/index.html')

def suma_resta(request):

    

    return render(request, 'calculadora/Suma_Resta.html')