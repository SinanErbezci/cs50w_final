from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    hello = "hello, world"
    output = {"hello" : hello}
    return render(request, "library/index.html",output)

def create_book(request):
    return HttpResponse("create book page")