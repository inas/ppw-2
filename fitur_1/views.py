from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
import json

response = {}

def index(request):
    response['author'] = 'Sheila Rezkia'
    html = 'fitur_1/fitur_1.html'
    return render(request, html, response)