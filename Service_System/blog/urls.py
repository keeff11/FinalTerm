from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('asd', views.post_list2, name='post_list2'),
    path('api_root/', include(router.urls)),
    path('abc', views.abc_view),
]