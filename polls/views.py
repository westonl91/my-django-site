from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
        return HttpResponse("Hello, everyone. I'm Leah. Can I put <h1>HTML</h1> in here?")
