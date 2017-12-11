"""lingin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
import fitur_1.urls as fitur_1
import fitur_2.urls as fitur_2
# import fitur_3.urls as fitur_3
# import fitur_4.urls as fitur_4


urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^fitur-1/', include(fitur_1, namespace='fitur-1')),
    url(r'^fitur-2/', include(fitur_2,namespace='fitur-2')),
 #    url(r'^fitur-3/', include(fitur_3,namespace='fitur-3')),
	# url(r'^fitur-4/', include(fitur_4,namespace='fitur-4')),
	url(r'^$', RedirectView.as_view(url='fitur-1/'))
]
