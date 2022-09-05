from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def familiares(request):
    padre=Familia(nombre="Agustin", apellido="Gittardi", Edad="50", relacion="padre", cumple="1971-09-27")
    madre=Familia(nombre="Marisa", apellido="Avaro", Edad="51", relacion="madre", cumple="1970-01-29")
    pareja=Familia(nombre="Tamara", apellido="Fugazza", Edad="25", relacion="pareja", cumple="1997-03-24")
    padre.save()
    madre.save()
    pareja.save()
    texto=f"{padre}, {madre}, {pareja}"
    return HttpResponse(texto)

