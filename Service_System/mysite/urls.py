from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token #added

urlpatterns = [
    path('admin/', admin.site.urls),  # a)
    path('', include('blog.urls')),
    path('api-token-auth/', obtain_auth_token), #added
]

# 정적 파일 및 미디어 URL 패턴 추가
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)