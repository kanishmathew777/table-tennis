from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from .views import PlayerViewSet, GroupViewSet, LoginViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'groups', GroupViewSet)

user_list = PlayerViewSet.as_view({'get': 'list','post': 'create'})

group_list = GroupViewSet.as_view({'get': 'list', 'post': 'create'})

urlpatterns = [
    path('', include(router.urls)),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
