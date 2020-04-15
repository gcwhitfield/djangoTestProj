from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse(open('./testproj/html/home.html', 'r'))