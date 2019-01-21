from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, MatchViewSet, SetViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'sets', SetViewSet)

team_list = TeamViewSet.as_view({'get': 'list', 'post': 'create'})

match_list = MatchViewSet.as_view({'get': 'list', 'post': 'create'})

set_list = SetViewSet.as_view({'get': 'list','post': 'create'})

urlpatterns = [
    path('', include(router.urls)),
]
