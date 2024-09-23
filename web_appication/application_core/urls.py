"""
Пути с доменными моделями для приложений
"""
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include("tinymce.urls")),
    # path('accounts/', include('django.contrib.auth.urls')),  # Встроенные URLs для авторизации
    path('', include('auth_app.urls')),
    path('', include('skills_viewer.urls')),
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth/', include("djoser.urls.authtoken")),
    # path('api/v1/auth/', include("djoser.urls.jwt")),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    path("__debug__/", include("debug_toolbar.urls")),
]

# Путь для выдачи медиа контента
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        re_path(r"^static/(?P<path>.*)$", views.serve),
    ]

urlpatterns += staticfiles_urlpatterns()

# Установка заголовков для админ панели
admin.site.site_header = "Digitalprofessional.me Панель администратора"
admin.site.site_title = "Панель администратора DPM"
admin.site.index_title = "Управление сайтом"