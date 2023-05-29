from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("This is Index")

def about(request):
    return HttpResponse("This is about")

def projects(request):
    return HttpResponse("This is my projects")

def contact(request):
    return HttpResponse("This is contact")
