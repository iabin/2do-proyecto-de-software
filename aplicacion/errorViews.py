from django.shortcuts import render


def noEncontrado(request):
    return render(request,'noEncontrado.html')

