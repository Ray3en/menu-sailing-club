from django.contrib import admin
from django.urls import path, include
from .views import menu_view, menu_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('menu/', menu_view, name='menu'),
    path('menu-page/', menu_page, name='menu-page'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
