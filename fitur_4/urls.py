from django.conf.urls import url
from .views import message_post



urlpatterns = [

    url(r'^add_message', message_post, name='add_message'),

 ]