from django.shortcuts import render
<<<<<<< HEAD
import matplotlib.pyplot as plt
import io
import urllib, base64
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
from random import sample
from io import StringIO
from calculadora.motores import SumaResta
<<<<<<< HEAD
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
=======
>>>>>>> 2f58eb675e00601073510361d0c9d645d1b7c7e3


def index(request):
    return render(request,'calculadora/index.html')

<<<<<<< HEAD
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
=======
def primerCorte(request):
    return render(request, 'calculadora/cortes/corte1.html')

def segundoCorte(request):
    return render(request, 'calculadora/cortes/corte2.html')

def tercerCorte(request):
    return render(request, 'calculadora/cortes/corte3.html')



def monteCarlo(request):
    figure = plt.gcf()
    buf = io.BytesIO()
    figure.savefig(buf, format='png', transparent=True, quality=100, dpi=200)
    buf.seek(0)
    imsrc = base64.b64encode(buf.read())
    imuri = 'data:image/png;base64,{}'.format(urllib.parse.quote(imsrc))
    return render(request, 'calculadora/monteCarlo.html', {'graphic':imuri})

def grafica(request):
    x = range(-10,10)
    y = sample(range(20), len(x))

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    # Creamos los ejes
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes.plot(x, y)
    axes.set_xlabel("Eje X")
    axes.set_ylabel("Eje Y")
    axes.grid()
    axes.axhline(0, color="black")
    axes.axvline(0, color="black")
    axes.set_title("Grafica de la funcion")
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response
>>>>>>> 2f58eb675e00601073510361d0c9d645d1b7c7e3
