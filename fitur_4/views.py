from django.shortcuts import render
from .forms import Message_Form
from .models import Tanggapan

def add_tanggapan(request):
	tanggapan_all=reversed(Tanggapan.objects.all())
	response['description'] = tanggapan_all
	html = 'fitur_4/fitur_4.html'
	response['message_form'] = Message_Form
	form = Message_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['description'] = request.POST['description']
		tanggapan_all = Tanggapan(tanggapanTwitter=response['description'], tanggapanSkype=response['description'], created_date_Twitter = datetime.now(), created_date_Skype=datetime.now())
		tanggapan_all.save()
		return HttpResponseRedirect('/fitur-1/')
	else:
		return HttpResponseRedirect('/fitur-1/')

