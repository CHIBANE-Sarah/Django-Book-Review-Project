from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("Application Bonnes Lectures,developpée en TP de Framework Web par -Sarah CHIBANE- Université d'Orléans, 2025")
