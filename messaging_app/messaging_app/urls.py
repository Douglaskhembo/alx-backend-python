from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),           # include chats app urls at /api/
    path('api-auth/', include('rest_framework.urls')),  # enable login/logout views for browsable API
]
