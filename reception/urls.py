from django.conf.urls import url
from . import views
from Diploma.views import *


urlpatterns = [
    url(r'^(?P<id_d>[\w-]+)/$', views.receptioninfo, name='reception_info'),
    url(r'^$', views.reception, name='reception'),
]
