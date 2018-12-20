from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^new/$', views.new, name="new"),
  url(r'^ajax_new/$', views.ajax_new, name="ajax_new"),
  url(r'^create/$', views.create, name="create"),
  url(r'^ajax_create/$', views.ajax_create, name="ajax_create"),
  url(r'^(?P<ticket_id>\d+)/show/$', views.show, name="show"),
  url(r'^(?P<ticket_id>\d+)/edit/$', views.edit, name="edit"),
  url(r'^(?P<ticket_id>\d+)/update/$', views.update, name="update"),
  url(r'^(?P<ticket_id>\d+)/delete/$', views.delete, name="delete"),
]