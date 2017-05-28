from __future__ import print_function
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def test(request):
    return HttpResponse("test")


def test2(request):
    return HttpResponse("test2")