from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
import json

response = {}

def index(request):
    response['author'] = 'Anisha Inas'
    html = 'fitur_2/fitur_2.html'
    return render(request, html, response)