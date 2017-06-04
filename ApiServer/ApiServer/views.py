from __future__ import print_function
from django.http import HttpResponse
from webhook.models import Log
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render
from urllib import parse
from pymongo import MongoClient
import json

import pymongo


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
    answer = {
        "speech": 'hi, I am fine. Thank you. and you? ',
        "displayText": 'hi, I am fine. Thank you. and you?',
        "source": "apiai-weather-webhook-sample"
    }
    ans_str = json.dumps(answer)
    return HttpResponse(ans_str)


def log(request):
    logs = Log.objects.all()
    return render(request, 'log.html', {'logs':logs})


def select(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test
    users = db.users

    print_string = "";
    for user in users.find():
        print_string += user["_id"] + ", " + user["city"] + "<br />"

    return HttpResponse(print_string)


def insert(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test
    users = db.users

    user = {"_id": "Mike", "city": "seoul"}
    try:
        user_id = users.insert(user)
    except pymongo.errors.DuplicateKeyError as e:
        return HttpResponse("Already exist.")

    return HttpResponse(user_id)


def delete(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test
    users = db.users

    users.remove({"_id": "Mike"})
    return HttpResponse("success")


def drop(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test
    users = db.users
    users.drop()
    return HttpResponse("success")
