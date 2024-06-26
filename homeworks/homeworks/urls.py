"""
URL configuration for homeworks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homework1/', include('homework1.urls')),
    path('homework2/', include('homework2.urls')),
    path('homework3/', include('homework3.urls')),
    path('homework4/', include('homework4.urls')),
    path('homework5/', include('homework5.urls')),
    path('__debug__/', include("debug_toolbar.urls")),
]
