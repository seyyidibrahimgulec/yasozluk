from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SignupForm
from contents.models import Entry 
from contents.views import HomePageListView
from interactions.models import Vote, Favorite


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

        
class UserProfileEntryView(HomePageListView):
    template_name = 'user_profile.html'
    paginate_by = 5
    context_object_name = "entries"

    def get_queryset(self):
        return (
            Entry.objects.filter(created_by=self.request.user).order_by("-created_at")
        )


class UserProfileVoteView(HomePageListView):
    template_name = 'user_profile.html'
    paginate_by = 5
    context_object_name = "votes"

    def get_queryset(self):
        return (
            Vote.objects.filter(user=self.request.user).order_by("-created_at")
        )


class UserProfileFavoriteView(HomePageListView):
    template_name = 'user_profile.html'
    paginate_by = 5
    context_object_name = "favorites"

    def get_queryset(self):
        return (
            Favorite.objects.filter(user=self.request.user).order_by("-created_at")
        )
