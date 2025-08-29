"""
URL configuration for TrainBase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView,DetailView
from django.conf import settings
from django.conf.urls.static import static

from viewer.views import EbookCreateView, AuthorCreateView, EbookListView, EbookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('aboutme/', TemplateView.as_view(template_name='about_me.html'), name='about_me'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),



    path('ebook/create/', EbookCreateView.as_view(), name='ebook_create'),
    path('ebook/list/', EbookListView.as_view(), name='ebook_list'),
    path('ebook/<int:pk>/', EbookDetailView.as_view(), name='ebook_detail'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
