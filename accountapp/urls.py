from django.urls.conf import path
from django.urls.resolvers import URLPattern
from django.urls import path
from accountapp.views import hello_world

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
