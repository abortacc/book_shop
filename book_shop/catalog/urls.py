from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog_main'),
    path('<slug:slug_name>/', views.catalog, name='catalog_category')
]
