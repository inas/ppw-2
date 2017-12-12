from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
import os
import json

response = {}

def index(request):
    response['author'] = 'Anisha Inas'
    html = 'fitur_2/fitur_2.html'
    print ("#==> profile")
    # ## sol : bagaimana cara mencegah error, jika url profile langsung diakses
    # if 'user_login' not in request.session.keys():
    #     return HttpResponseRedirect(reverse('fitur-1:index'))
    # ## end of sol

    # set_data_for_session(response, request)

    return render(request, html, response)