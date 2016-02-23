from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^topics/$', views.TopicView.as_view(
        { 'get': 'list' }
    ), name='topic'),

    url(r'^topics/(?P<pk>\d+)$', views.TopicView.as_view(
        { 'get': 'retrieve' }
    ), name='topic-list')
]
