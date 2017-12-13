from django.conf.urls import url
from .views import add_tanggapan

urlpatterns = [
 	url(r'add_tanggapan/$', add_tanggapan, name='add_tanggapan'),
]