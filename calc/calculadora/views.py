from django.shortcuts import render, redirect
from django.http import HttpResponse
def calc(request):
    return render(request, 'index.html')