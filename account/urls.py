from django.conf.urls import url
from . import views
from reception.views import *


urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^(?P<pat>[\w-]+)/$', patientinfo, name='information_patient'),
    url(r'^history/(?P<pat>[\w-]+)/$', newhistory, name='history'),
    url(r'^alergik/(?P<pat>[\w-]+)/$', newalergik, name='alergik'),
    url(r'^operation/(?P<pat>[\w-]+)/$', newoperation, name='operation'),
    url(r'^chronik/(?P<pat>[\w-]+)/$', newchronik, name='chronik'),
    url(r'^graft/(?P<pat>[\w-]+)/$', newgraft, name='graft'),
]
