from django.urls import path
from . import views
from .statistiques import* 

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
    path('api/biens/', views.BienList.as_view(), name='bien-list'),
    path('api/biens/<int:pk>/', views.BienDetail.as_view(), name='bien-detail'),

    # Routes pour les chambres (Chambre)
    path('api/chambres/', views.ChambreList.as_view(), name='chambre-list'),
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
]
