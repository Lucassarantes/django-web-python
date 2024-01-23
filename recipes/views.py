from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Lucas Salles',
    })

def contact(request):
    return render(request, 'me-apague/temp.html')

def about(request):
    return HttpResponse('ABOUT')