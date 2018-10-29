from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def noticias(request):
    return render(request,'noticias.html')

def listaCursos(request):
    return render(request,'listaCursos.html')

def disciplina(request):
    return render(request,'disciplina.html')

def detalheCurso(request):
    return render(request,'detalheCurso.html')
# Create your views here.
