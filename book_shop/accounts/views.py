from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView, RedirectView, ListView
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from .forms import ProfileEditForm


User = get_user_model()


class ProfileTemplateView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_own_profile'] = self.object == self.request.user
        return context


class EditProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'accounts/edit_profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse(
            'accounts:profile',
            kwargs={'username': self.request.user.username}
        )


class FollowUserView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user_to_follow = get_object_or_404(User, username=self.kwargs['username'])
        if self.request.user != user_to_follow:
            self.request.user.followers.add(user_to_follow)
        return reverse('accounts:profile', kwargs={'username': self.kwargs['username']})


class UnfollowUserView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user_to_unfollow = get_object_or_404(User, username=self.kwargs['username'])
        self.request.user.followers.remove(user_to_unfollow)
        return reverse('accounts:profile', kwargs={'username': self.kwargs['username']})


class FollowersListView(ListView):
    model = User
    template_name = 'accounts/followers_list.html'
    context_object_name = 'followers'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.followers.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, username=self.kwargs['username'])
        return context


class FollowingListView(ListView):
    model = User
    template_name = 'accounts/following_list.html'
    context_object_name = 'following'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.following.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, username=self.kwargs['username'])
        return context
