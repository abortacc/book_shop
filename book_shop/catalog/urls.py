from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='catalog_main'),
    path(
        '<slug:slug_name>/',
        views.CatalogListView.as_view(),
        name='catalog_category'
    ),
    path('details/<int:pk>/', views.BookDetailView.as_view(), name='details'),
    path(
        'details/<int:pk>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(
        'details/<int:pk>/edit_comment/<int:comment_id>/',
        views.CommentUpdateView.as_view(),
        name='edit_comment'
    ),
    path(
        'details/<int:pk>/delete_comment/<int:comment_id>/',
        views.CommentDeleteView.as_view(),
        name='delete_comment'
    ),
]
