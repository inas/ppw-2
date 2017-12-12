from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import Message_Form
from .models import Message

# Create your views here.

response = {}



def index(request):
	response['author']= "Widya Syafira"
	html = 'fitur_3/fitur_3.html'
	return render(request, html, response)

def dashboard(request, pengguna):
    message = Message.objects.filter(pengguna=pengguna)
   
    response['message'] = message
    response['message_form'] = Message_Form
    response["message_list"] = message
    print("kkkkkk"+ str(message))
    html = 'fitur_3/fitur_3.html'

    message_list = message
    paginator = Paginator(message_list, 5)
    page = request.GET.get('page', 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
   
    response["message_list"] = users
    html = 'fitur_3/fitur_3.html'
    return render(request, html, response)


def add_message(request):
	form = Message_Form(None or request.POST )

	if (request.method == 'POST' and form.is_valid()):
		response['pengguna'] = 13101373
		response['title'] = request.POST['title'] 
		response['message'] = request.POST['message']
		message = Message(pengguna=13601373,title= response['title'], message= response['message'])
		message.save()
		html ='fitur_3/fitur_3.html'    
		return HttpResponseRedirect('/fitur-3/')
	else :
		return HttpResponseRedirect('/fitur-3/')

def paginate_page(page, data_list):
	paginator = Paginator(data_list, 5)

	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)

	# Get the index of the current page
	index = data.number - 1
	# This value is maximum index of your pages, so the last page - 1
	max_index = len(paginator.page_range)
	# You want a range of 10, so lets calculate where to slice the list
	start_index = index if index >= 5 else 0
	end_index = 5 if index < max_index - 5 else max_index
	# Get our new page range. In the latest versions of Django page_range returns 
	# an iterator. Thus pass it to list, to make our slice possible again.
	page_range = list(paginator.page_range)[start_index:end_index]
	paginate_data = {'data':data, 'page_range':page_range}
	return paginate_data