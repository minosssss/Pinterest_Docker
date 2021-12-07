from django.urls import path

from subscribeapp.views import SubscriptioinView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/',SubscriptioinView.as_view(), name='subscribe'),
]