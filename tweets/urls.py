from django.urls import path

from django.views.generic.base import RedirectView

from .views import (
    RetweetView,
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView,
    TweetListView,
    TweetUpdateView
    )

app_name = 'tweets'

urlpatterns = [
    path('', RedirectView.as_view(url="/")),
    path('search/', TweetListView.as_view(), name='list'), # /tweet/
    path('create/', TweetCreateView.as_view(), name='create'), # /tweet/create/
    path('<pk>/', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    path('<pk>/retweet/', RetweetView.as_view(), name='detail'), # /tweet/1/
    path('<pk>/update/', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    path('<pk>/delete/', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]
