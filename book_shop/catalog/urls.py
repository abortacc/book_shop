from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog_main'),
    path('category/<slug:slug_name>/', views.category, name='catalog_category')
]
