from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^hello-world$', views.hello_world, name='hello-world'),
]