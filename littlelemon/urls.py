"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App-level URLs
    path('', include('restaurant.urls')),

    # Djoser Authentication and Registration paths
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # Support /api/ for authentication too
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
]
