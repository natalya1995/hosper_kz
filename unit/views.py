from django.shortcuts import render,redirect
from .models import Smokehouse,Hosper,Stand
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, './client/home.html')

def category_page(request):
    return render(request, './client/category.html')

def stand_list(request):
    stands = Stand.objects.all()
    return render(request, './client/stand_list.html', {'stands': stands})

def stand_detail(request, slug):
    stand = get_object_or_404(Stand, slug=slug)
    return render(request, './client/stand_detail.html', {'stand': stand})

def hosper_list(request):
    hospers = Hosper.objects.all()
    return render(request, './client/hosper_list.html', {'hospers': hospers})

def hosper_detail(request, slug):
    hosper = get_object_or_404(Hosper, slug=slug)
    return render(request, './client/hosper_detail.html', {'hosper': hosper})

def smokehouse_list(request):
    smokehouses = Smokehouse.objects.all()
    return render(request, './client/smokehouse_list.html', {'smokehouses': smokehouses})

def smokehouse_detail(request, slug):
    smokehouse = get_object_or_404(Smokehouse, slug=slug)
    return render(request, './client/smokehouse_detail.html', {'smokehouse': smokehouse})