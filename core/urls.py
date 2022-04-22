from os import stat
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('work/', include('work.urls', namespace="work")),
    path('people/', include('people.urls', namespace="people")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    