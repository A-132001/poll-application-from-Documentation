from django.shortcuts import render

from django.http import HttpResponse 

def firstview(request):
    return HttpResponse("Hello World")