
from django.urls import path, include
from game.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('tournaments', TournamentViewSet, basename='tournaments')
router.register('players', PlayerViewSet, basename='players')
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns = urlpatterns + router.urls
