from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.ProfileTemplateView.as_view(), name='profile'),
    path(
        'edit-profile/',
        views.EditProfileUpdateView.as_view(),
        name='edit_profile'
    ),
]
