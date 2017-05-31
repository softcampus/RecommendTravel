from __future__ import print_function
from django.http import HttpResponse
from webhook.models import Log
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render
from urllib import parse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def test(request):
    return HttpResponse("test")


def test2(request):
    return HttpResponse("test2")

@csrf_exempt
@require_POST
def webhook(request):
    received_json_data = request.body.decode("utf-8")
    received_json_data = parse.unquote(received_json_data)
    log = Log(json_data = received_json_data)
    log.save()
    return HttpResponse(received_json_data)

def log(request):
    logs = Log.objects.all()
    return render(request, 'log.html', {'logs':logs})
