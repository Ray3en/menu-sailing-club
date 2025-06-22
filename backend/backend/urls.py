from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myapp.views import menu_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('myapp.urls'))
    path('', menu_page, name='menu-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)