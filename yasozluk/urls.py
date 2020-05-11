"""yasozluk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from contents.api_views import CreateEntryAPIView
from contents.views import HomePageListView, EntryListView, NewTopicView, today_in_history, TopicSearchListView, ChannelTopicsListView
from interactions.views import MessageCreate, MessagesView, NewMessageView, get_message_history, get_message_poll, \
    poll_message_count
from users.views import SignupView, UserProfileEntryView, UserProfileFavoriteView, UserProfileVoteView
from interactions.api_views import CreateFavoriteAPIView, CreateVoteAPIView, DestroyVoteAPIView, DestroyFavoriteAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('messages/<int:user_id>/<str:slug>/', MessagesView.as_view(), name="messagesRoute"),
    path('messages/', MessagesView.as_view(), name="allMessages"),
    path('messages/new/', NewMessageView.as_view(), name="newMessage"),
    path('ajax/messages/new/', login_required(MessageCreate.as_view()), name="newMessageAjax"),
    path('ajax/messages/count', poll_message_count, name="messageCountAjax"),
    path('ajax/messages/get', get_message_poll, name="messageGetAjax"),
    path('ajax/messages/history', get_message_history, name="messageHistoryGetAjax"),
    path("", HomePageListView.as_view(), name="home"),
    path("topic/<int:topic_pk>/", EntryListView.as_view(), name="topic_entries"),
    path("topic/new/", NewTopicView.as_view(), name="new_topic"),
    path("user_profile/entries/", UserProfileEntryView.as_view(), name="user_entries"),
    path("user_profile/votes/", UserProfileVoteView.as_view(), name="user_votes"),
    path("user_profile/favorites/", UserProfileFavoriteView.as_view(), name="user_favorites"),
    url(r'^ajax/today', today_in_history, name='today'),
    path("topic_search/", TopicSearchListView.as_view(), name="topic_search"),
    path("channel/<int:channel_pk>/", ChannelTopicsListView.as_view(), name="channel_topics"),
]


urlpatterns += [
    path("api/new_entry/", CreateEntryAPIView.as_view(), name="new_entry"),
    path("api/new_vote/", CreateVoteAPIView.as_view(), name="new_vote"),
    path("api/new_favorite/", CreateFavoriteAPIView.as_view(), name="new_favorite"),
    path("api/vote/<int:pk>/", DestroyVoteAPIView.as_view(), name="delete_vote"),
    path("api/favorite/<int:pk>/", DestroyFavoriteAPIView.as_view(), name="delete_favorite"),
]
