"""
URL configuration for USMPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import django.conf.urls as conf_urls
import BlogApp.views as blog_views
from django.conf.urls.static import static
from django.conf import settings
import os
import json
OS_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRETS_FILE = os.path.join(OS_BASE_DIR, "secrets.json")

with open(SECRETS_FILE) as file:
    secrets = json.load(file)

urlpatterns = [
    path(f"{secrets["admin_route"]}/", admin.site.urls),
    path("", include("BlogApp.urls"), name='blog-urls')
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)


conf_urls.handler400 = blog_views.custom_404