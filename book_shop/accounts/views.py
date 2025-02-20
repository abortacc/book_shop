from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView
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
