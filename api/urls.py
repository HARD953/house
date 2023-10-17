from django.urls import path
from . import views
from .statistiques import* 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Documentation for your APIs",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="issa97403@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Routes pour les équipements (Equipement)
    path('api/equipements/', views.EquipementList.as_view(), name='equipement-list'),
    path('api/equipements/<int:pk>/', views.EquipementDetail.as_view(), name='equipement-detail'),

    # Routes pour les services (Service)
    path('api/services/', views.ServiceList.as_view(), name='service-list'),
    path('api/services/<int:pk>/', views.ServiceDetail.as_view(), name='service-detail'),

    # Routes pour les images (Image)
    path('api/images/', views.ImageList.as_view(), name='image-list'),
    path('api/images/<int:pk>/', views.ImageDetail.as_view(), name='image-detail'),

    # Routes pour les biens (Bien)
    path('api/bienscreate/', views.BienCreate.as_view(), name='bien-create'),
    path('api/bienslist/', views.BienList.as_view(), name='bien-list'),
    path('api/biens/<int:pk>/', views.BienDetail.as_view(), name='bien-detail'),

    # Routes pour les chambres (Chambre)
    path('api/chambrescreate/', views.ChambreCreate.as_view(), name='chambre-create'),
    path('api/chambreslist/', views.ChambreList.as_view(), name='chambre-list'),
    path('api/chambres/<int:pk>/', views.ChambreDetail.as_view(), name='chambre-detail'),

    # Routes pour les réservations (Reservation)
    path('api/reservations/', views.ReservationList.as_view(), name='reservation-list'),
    path('api/reservations/<int:pk>/', views.ReservationDetail.as_view(), name='reservation-detail'),

    # Routes pour les commentaires (Commentaire)
    path('api/commentaires/', views.CommentaireList.as_view(), name='commentaire-list'),
    path('api/commentaires/<int:pk>/', views.CommentaireDetail.as_view(), name='commentaire-detail'),

    # Routes pour les transactions (Transaction)
    path('api/transactions/', views.TransactionList.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),

    path('api/totaloccupation/', OccupancyRate.as_view(), name='occupation-rate'),
    path('api/totalreservation/', TotalReservations.as_view(), name='reservation-rate'),
    path('api/totalreservations/', ReservationsByMonthYear.as_view(), name='reservations-rate'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
