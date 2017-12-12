from django.conf.urls import url
from .views import index, add_message, dashboard

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_message/', add_message, name='add_message'),
	url(r'^dashboard/(?P<pengguna>.*)/$', dashboard, name='dashboard'),


]

