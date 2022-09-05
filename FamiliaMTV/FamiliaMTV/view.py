from django.http import HttpResponse
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.template import loader
def saludar (request):
    return HttpResponse("hola mundo")

def template1(self):
    nomb= "Santiago"
    apell= "Gittardi"
    cumpleaños="17 de marzo"

    diccionario={'nombre':nomb, 'apellido':apell}
    plantilla= loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
