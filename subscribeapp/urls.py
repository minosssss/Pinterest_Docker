from django.urls import path

from subscribeapp.views import SubscriptioinView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/',SubscriptioinView.as_view(), name='subscribe'),
    path('list/',SubscriptionListView.as_view(), name='list'),
]