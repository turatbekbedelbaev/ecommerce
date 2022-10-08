"""Конфигурация URL-адреса электронной торговли

Список urlpatterns направляет URL-адреса в представления. Для получения дополнительной информации см .:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Примеры:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app
    2. Добавьте URL-адрес в urlpatterns: path ('', views.home, name = 'home')
Представления на основе классов
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL-адрес в urlpatterns: path ('', Home.as_view (), name = 'home')
Включение другого URLconf
    1. Импортируйте функцию include (): из импорта django.urls include, path
    2. Добавьте URL-адрес в urlpatterns: path ('blog /', include ('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)