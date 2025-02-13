from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='homepage')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('profile/', include('accounts.urls', namespace='accounts')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('homepage:index')
        ),
        name='registration',
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
