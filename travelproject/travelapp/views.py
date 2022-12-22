from django.http import HttpResponse
from django.shortcuts import render
from .models import People

# Create your views here.

def demo(req):
    obj = People.objects.all()
    return render(req, "index.html", {'result': obj})

# def about(req):
#     return HttpResponse("This is about page")
