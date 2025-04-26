from django.urls import path


from .views import (
    CartTemplateView,
    AddToCartView,
    UpdateCartItemView,
    CheckoutView,
    SuccessView
)


app_name = 'cart'


urlpatterns = [
    path('', CartTemplateView.as_view(), name='main'),
    path('add/<int:book_id>/', AddToCartView.as_view(), name='add'),
    path('update/<int:item_id>/', UpdateCartItemView.as_view(), name='update'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('success/', SuccessView.as_view(), name='success'),
]
