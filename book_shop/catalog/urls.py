from rest_framework.routers import DefaultRouter


from django.urls import include, path
from . import views


app_name = 'catalog'


router = DefaultRouter()
router.register('books', views.BookViewSet)
router.register('categories', views.CategoryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
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
