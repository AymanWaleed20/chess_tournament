from django.urls import path, include
from game.views import TournamentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tournaments', TournamentViewSet, basename='tournaments')

urlpatterns = [

]
urlpatterns = urlpatterns + router.urls
