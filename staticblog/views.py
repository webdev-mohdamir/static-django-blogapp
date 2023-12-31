from django.shortcuts import render
from . import data

def index(request):
    return render(request, 'index.html', {"data":data.data})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def post_1(request):
    return render(request, 'post_1.html', {"data": data.data[0]})

def post_2(request):
    return render(request, 'post_2.html', {"data": data.data[1]})

def post_3(request):
    return render(request, 'post_3.html', {"data": data.data[2]})

def post_4(request):
    return render(request, 'post_4.html', {"data": data.data[3]})