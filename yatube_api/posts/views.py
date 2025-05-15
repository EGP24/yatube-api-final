# Python
from django.urls import path, include

# Подключаем маршруты API
urlpatterns = [
    path("api/", include("api.urls")),
]
