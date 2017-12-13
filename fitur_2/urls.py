from django.conf.urls import url
from .views import index, add_company
from fitur_1.views import index as index1

urlpatterns = [
	url(r'^$', index1),
    url(r'^(?P<id>\d+)/$', index, name='index'),
    url(r'^add-company/$',add_company, name='add-company')
]