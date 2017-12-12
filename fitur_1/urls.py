from django.conf.urls import url
from .views import index, add_session, remove_session

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add-session/$', add_session, name='add-session'),
	url(r'^remove-session/$', remove_session, name='remove-session'),
]
