from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = 'HELLO WORLD'
    text = 'S MY FIRST DJANGO APP'
    return render(request,'./index.html', {'a': a, 'text': text})

