from django.urls import path
from .views import *

urlpatterns = [
    # Routes pour les équipements (Equipement)
    path('customer/', CustomUserList.as_view(), name='customuser-list'),
    path('customer/<int:pk>/', CustomUserDetail.as_view(), name='customuser-detail'),

    path('signup/', CustomUserSignUp.as_view(), name='customuser-signup'),
    path('login/', CustomUserLogin.as_view(), name='customuser-login'),
    path('logout/', CustomUserLogout.as_view(), name='customuser-logout')
]


