from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path(
        'edit-profile/',
        views.EditProfileUpdateView.as_view(),
        name='edit_profile'
    ),
    path('<slug:username>/', views.ProfileTemplateView.as_view(), name='profile'),
    path('<slug:username>/followers/', views.FollowersListView.as_view(), name='followers'),
    path('<slug:username>/following/', views.FollowingListView.as_view(), name='following'),
]
