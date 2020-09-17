from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('job/', include('job.urls', namespace='job')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
