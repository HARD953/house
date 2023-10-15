from django.urls import path
from . import views

urlpatterns = [
    # Routes pour les équipements (Equipement)
    path('api/customer/', views.CustomUserList.as_view(), name='customuser-list'),
    path('api/customer/<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
]
