from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.manage_authors, name='manage_authors'),
        # ex: /polls/
    #url(r'^$', views.manage_incidents, name='manage_incidents'),
)