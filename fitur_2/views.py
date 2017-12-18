from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import os
import json

response = {}

def index(request, id):
    response['login'] = True
    company = Company.objects.get(id__exact=id)
    response['name'] = company.name
    response['com_type'] = company.companyType
    response['website'] = company.website
    response['desc'] = company.desc
    response['specialities'] = company.specialities
    response['address'] = company.address
    # print("desc "+company.desc)
    # print("jadiii " + company.name)
    html = 'fitur_2/fitur_2.html/'
    return render(request, html, response)

@csrf_exempt
def add_company(request):
    id = request.POST.get('id')
    print(request.POST)
    print("comtype "+request.POST.get('specialties[values][]'))
    if (Company.objects.filter(id__exact=id).count()> 0):
        company = Company.objects.get(id__exact=id)
        company.desc = request.POST.get('description')
        company.companyType = request.POST.get('companyType[name]')
        company.website = request.POST.get('websiteUrl')
        company.desc = request.POST.get('description')
        company.specialities = request.POST.get('specialties[values][]')
        company.address = request.POST.get('locations[values][0][address][street1]')
    
        company.save()
        return HttpResponse(id)

    name = request.POST.get('name')
    com_type = request.POST.get('companyType[name]')
    website = request.POST.get('websiteUrl')
    desc = request.POST.get('description')
    specialities = request.POST.get('specialties[values][]')
    address = request.POST.get('locations[values][0][address][street1]')
    company = Company(id=id, name=name,companyType=com_type,website=website,desc=desc,address=address,specialities=specialities)
    company.save()
    return HttpResponse(id)