from django.conf.urls import url
from .views import index, add_company

urlpatterns = [
    url(r'^(?P<id>\d+)/$', index, name='index'),
    url(r'^add-company/$',add_company, name='add-company')
]