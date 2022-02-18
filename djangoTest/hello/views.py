from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reques):
    return HttpResponse("Hello, world. You're at the hello index. 안녕하세요")
