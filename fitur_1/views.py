from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
import json

response = {}

def index(request):
	response['author'] = 'Sheila Rezkia'
	html1 = 'fitur_1/fitur_1.html'
	return render(request, html1, response)

def add_session(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        request.session['user_login'] = id
        request.session['name'] = name
        try:
            user = User.objects.get(id = id)
        except Exception as e:
            user = User()
            user.id = id
            user.name = name
            user.save()
        return HttpResponseRedirect(reverse('fitur-2:index'))

def remove_session(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('fitur-2:index'))