from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^account/create', views.create_account),
    url(r'^account/get/(?P<pk>[0-50]+)', views.get_account),
    url(r'^account/update/(?P<pk>[0-50]+)', views.update_account),
    url(r'^account/delete/(?P<pk>[0-50]+)', views.delete_account),
    url(r'^match/create', views.create_match),
    url(r'^match/check/(?P<pk>[0-50]+)', views.check_match),
    url(r'^match/get/(?P<pk>[0-50]+)', views.get_all_match),
    url(r'^location/update', views.update_location),
    url(r'^find/get/(?P<pk>[0-50]+)', views.find_people),
)