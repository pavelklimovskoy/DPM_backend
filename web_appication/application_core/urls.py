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
    # path('favicon.ico', RedirectView.as_view(url=static('images/favicon.ico'))),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include("djoser.urls.authtoken")),
    path('api/v1/auth/', include("djoser.urls.jwt")),

    path('api/v1/news/', include("news_application.urls")),
    path('api/v1/about/', include("about_application.urls")),
    path('api/v1/profile/', include("profile_application.urls")),
    path('api/v1/cv/', include("cv_application.urls")),

    path('api/v1/rchilli/', include("rchilli_application.urls")),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/v1/state/', include("state_application.urls")),
    path('api/v1/', include("employee_application.urls")),

    path("__debug__/", include("debug_toolbar.urls")),

]

# Путь для выдачи медиа контента
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r"^static/(?P<path>.*)$", views.serve),
    ]

urlpatterns += staticfiles_urlpatterns()

# Установка заголовков доя админ панели
admin.site.site_header = "Digitalprofessional.me Панель администратора"
admin.site.site_title = "Панель администратора DPM"
admin.site.index_title = "Управление сайтом"
