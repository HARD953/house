from django.urls import path
from .views import *
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    # Routes pour les équipements (Equipement)
    path('customer/', CustomUserList.as_view(), name='customuser-list'),
    path('customer/<int:pk>/', CustomUserDetail.as_view(), name='customuser-detail'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),

    path('signup/', CustomUserLogin.as_view(), name='inscription'),
]


