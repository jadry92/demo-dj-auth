"""
URL configuration for project.

"""
# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main_app.home.urls")),
    path('users/', include('main_app.users.urls')),
    path('users/auth/', include('dj_rest_auth.urls')),
    path('users/auth/registration/', include('dj_rest_auth.registration.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
