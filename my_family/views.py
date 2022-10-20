from django.http import request
from django.shortcuts import render
def relative(request):
    return render(request, "App/relatives.html")
