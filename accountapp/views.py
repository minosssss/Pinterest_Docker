from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')