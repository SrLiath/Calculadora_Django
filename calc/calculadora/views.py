from django.shortcuts import render, redirect
from django.http import HttpResponse

def calc(request):
    return render(request, 'index.html')
    dn = 1
    numero = "0"
    while (dn == 1):
        if request.POST.get('add_numero(1)'):
            numero = numero + "1"
        elif request.POST.get('add_numero(2)'):
            numero = numero + "2"
        elif request.POST.get('add_numero(3)'):
            numero = numero + "3"
        elif request.POST.get('add_numero(4)'):
            numero = numero + "4"
        elif request.POST.get('add_numero(5)'):
            numero = numero + "5"
        elif request.POST.get('add_numero(6)'):
            numero = numero + "6"
        elif request.POST.get('add_numero(7)'):
            numero = numero + "7"
        elif request.POST.get('add_numero(8)'):
            numero = numero + "8"
        elif request.POST.get('add_numero(9)'):
            numero = numero + "9"
        elif request.POST.get('add_numero(0)'):
            numero = numero + "0"
        elif request.POST.get("add_operador('+')"):
            numero = numero + "+"
        elif request.POST.get("add_numero('.')"):
            numero = numero + "."
        elif request.POST.get("add_operador('-')"):
            numero = numero + "-"
        elif request.POST.get("add_operador('*')"):
            numero = numero + "*"
        elif request.POST.get("add_operador('/')"):
            numero = numero + "/"
        elif request.POST.get("total()"):
            eval(numero)
        elif request.POST.get("limpar()"):
            numero = "0"