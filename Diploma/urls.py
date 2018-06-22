from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^reform/$', views.reform, name='reform'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^information/$', views.inforamtion, name='cabinet'),
    url(r'^queue/$', views.myqueue, name='queue'),
    url(r'^download/(?P<rec>[\w-]+)/$', views.muqueuedownload, name='download'),
    url(r'^doctors_list/$', views.doctros_list, name='doctors_list'),
    url(r'^patient/', views.patient_list, name='patient_list'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^news/', include('other.urls')),
    url(r'^reception/', include('reception.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
