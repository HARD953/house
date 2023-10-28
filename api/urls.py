from django.urls import path
from . import views
from .statistiques import* 

urlpatterns = [
    # Routes pour les équipements (Equipement)
    path('equipements/', views.EquipementList.as_view(), name='equipement-list'),
    path('equipements/<int:pk>/', views.EquipementDetail.as_view(), name='equipement-detail'),

    # Routes pour les services (Service)
    path('services/', views.ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceDetail.as_view(), name='service-detail'),

    # Routes pour les images (Image)
    path('images/', views.ImageList.as_view(), name='image-list'),
    path('images/<int:pk>/', views.ImageDetail.as_view(), name='image-detail'),

    # Routes pour les biens (Bien)
    path('bienscreate/', views.BienCreate.as_view(), name='bien-create'),
    path('bienslist/', views.BienList.as_view(), name='bien-list'),
    path('biens/<int:pk>/', views.BienDetail.as_view(), name='bien-detail'),

    # Routes pour les chambres (Chambre)
    path('chambrescreate/', views.ChambreCreate.as_view(), name='chambre-create'),
    path('chambreshotel/', views.ChambreHotel.as_view(), name='chambre-hotel'),
    path('chambresresid/', views.ChambreResidence.as_view(), name='chambre-resid'),
    path('chambreshotelresid/', views.ChambreResidence.as_view(), name='hotel-resid'),
    path('chambres/<int:pk>/', views.ChambreDetail.as_view(), name='chambre-detail'),

    # Routes pour les réservations (Reservation)
    path('reservations/', views.ReservationList.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', views.ReservationDetail.as_view(), name='reservation-detail'),

    # Routes pour les commentaires (Commentaire)
    path('commentaires/', views.CommentaireList.as_view(), name='commentaire-list'),
    path('commentaires/<int:pk>/', views.CommentaireDetail.as_view(), name='commentaire-detail'),

    # Routes pour les transactions (Transaction)
    path('transactions/', views.TransactionList.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),

    path('totaloccupation/', OccupancyRate.as_view(), name='occupation-rate'),
    path('totalreservation/', TotalReservations.as_view(), name='reservation-rate'),
    path('totalreservations/', ReservationsByMonthYear.as_view(), name='reservations-rate'),
]
