from django.shortcuts import render
from calculadora.motores import SumaResta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


def index(request):

    return render(request,'calculadora/index.html')

def suma_resta(request):
    return render(request, 'calculadora/Suma_Resta.html')
@csrf_exempt 
def calcSumRest(request):
    if request.is_ajax() and request.method == 'POST':
        #print("respuesta : ", dict(request.POST.get('dats'))['mUno'])
        mDos = json.loads(request.POST.get('dats'))['mUno']
        #mDos = json.loads(request.POST.get('dats')[1])

        return JsonResponse({'m':mDos, 'success':True})
    
    return JsonResponse({'success':False})
