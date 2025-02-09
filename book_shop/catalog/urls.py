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
    path('details/<int:pk>/', views.details, name='details')
]
