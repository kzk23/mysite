"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path
from . import views
from django.urls import re_path
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap

from .sitemaps import (
    BlogPostSitemap,
    StaticViewSitemap,
)

sitemaps = {
    'blog': BlogPostSitemap,
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('', views.top, name='top'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
