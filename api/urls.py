from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import GameOfThronesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/game-of-thrones/', GameOfThronesView.as_view(), name='game_of_thrones'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
