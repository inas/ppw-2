from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import os
import json

response = {}

def index(request, id):
    response['login'] = True
    company = Company.objects.get(id__exact=id)
    response['name'] = company.name
    response['com_type'] = company.com_type
    response['website'] = company.website
    response['logo_url'] = company.logo_url
    response['desc'] = company.desc
    response['specialities'] = company.specialities
    response['address'] = company.address
    print(company.specialities)
    html = 'fitur_2/fitur_2.html/'
    return render(request, html, response)

@csrf_exempt
def add_company(request):
    id = request.POST.get('id')

    if (Company.objects.filter(id__exact=id).count()> 0):
        return HttpResponse(id)

    name = request.POST.get('name')
    com_type = request.POST.get('com_type')
    website = request.POST.get('website')
    logo_url = request.POST.get('logo_url')
    desc = request.POST.get('desc')
    specialities = request.POST.get('specialities')
    print(specialities)
    address = request.POST.get('address')
    company = Company(id=id, name=name,com_type=com_type,website=website,logo_url=logo_url,desc=desc,address=address)
    company.save()
    return HttpResponse(id)