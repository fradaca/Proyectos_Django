from django.http import HttpResponse

from django.template import Template,Context

from django.shortcuts import render

from django.shortcuts import loader
class Persona(object):

    def __init__(self,nombre,edad,rol):

        self.nombre=nombre

        self.edad=edad

        self.rol=rol

def saludo(request):

    Mi_persona=Persona("Franco Daniel Capra",23,"Ayudante")

    Lista_de_temas=["Condicionales","Control de flujo","Listas","Tuplas y diccionarios","Funciones"]

    Diccionario_plantilla={"mi_nombre":Mi_persona.nombre,"mi_edad":Mi_persona.edad,"mi_rol":Mi_persona.rol,"lista_temas":Lista_de_temas}

    documento_externo=loader.get_template("Plantilla_base.html")

    documento_cargado=documento_externo.render(Diccionario_plantilla)

    return HttpResponse(documento_cargado)

def Plantilla_Heredada(request):

    return render(request,"CursoC.html")