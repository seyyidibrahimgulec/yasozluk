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
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from contents.views import HomePageListView
from contents.views import entryListView, newTopic
from interactions.views import messages, newMessage
from users.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('topic/<int:num>/', entryListView, name="topicEntries"),
    path('messages/<int:user_id>/<str:slug>/', messages, name="messagesRoute"),
    path('messages/', messages, name="allMessages"),
    path('topic/new', newTopic, name="newTopic"),
    path('messages/new/', newMessage, name="newMessage"),
    path("", HomePageListView.as_view(), name="home"),
]
