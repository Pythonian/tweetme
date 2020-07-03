from django.urls import path

from django.views.generic.base import RedirectView

from .views import (
    LikeToggleAPIView,
    RetweetAPIView,
    TweetCreateAPIView,
    TweetListAPIView,
    TweetDetailAPIView,

    )

app_name = 'tweet-api'

urlpatterns = [
    path('', TweetListAPIView.as_view(), name='list'), # /api/tweet/
    path('create/', TweetCreateAPIView.as_view(), name='create'), # /tweet/create/
    path('<pk>/', TweetDetailAPIView.as_view(), name='detail'),
    path('<pk>/like/', LikeToggleAPIView.as_view(), name='like-toggle'),
    path('<pk>/retweet/', RetweetAPIView.as_view(), name='retweet'), #/api/tweet/id/tweet/
]
