from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^users/$', views.UserView.as_view(
        { 'get': 'list' }
    ), name='user-list'),

    url(r'^users/(?P<pk>\d+)$', views.UserView.as_view(
        { 'get': 'retrieve' }
    ), name='user')
]
