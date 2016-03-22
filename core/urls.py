from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^topics/?$', views.TopicView.as_view(
        { 'get': 'list' }
    ), name='topic-list'),

    url(r'^topics/(?P<pk>\d+)$', views.TopicView.as_view(
        { 'get': 'retrieve' }
    ), name='topic'),

    url(r'^threads/?$', views.ThreadView.as_view(
        { 'get': 'list', 'post': 'create' }
    ), name='thread-list'),

    url(r'^threads/(?P<pk>\d+)$', views.ThreadView.as_view(
        { 'get': 'retrieve' }
    ), name='thread'),

    url(r'^comments/?$', views.CommentView.as_view(
        { 'get': 'list', 'post': 'create' }
    ), name='comment-list'),

    url(r'^comments/(?P<pk>\d+)$', views.CommentView.as_view(
        { 'get': 'retrieve' }
    ), name='comment')
]
