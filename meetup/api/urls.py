from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^account/create', views.create),
    url(r'^account/get/(?P<pk>[0-9]+)', views.get),
    url(r'^account/update/(?P<pk>[0-9]+)', views.update),
    url(r'^account/delete/(?P<pk>[0-9]+)', views.delete),
)