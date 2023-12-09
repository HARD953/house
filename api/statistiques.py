# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import *
# from django.db.models import*
# from django.db.models.functions import*

# class TotalReservations(APIView):
#     def get(self, request):
#         total_reservations = Reservation.objects.count()
#         # total_revenue = Reservation.objects.aggregate(Sum('prix_total'))['prix_total__sum']
#         # property_types = Bien.TYPES_CHOICES
#         # reservations_by_type = {}
#         # for property_type, _ in property_types:
#         #     reservations_count = Reservation.objects.filter(bien__type=property_type).count()
#         #     reservations_by_type[property_type] = reservations_count
#         # status_choices = Reservation.STATUT_CHOICES
#         # reservations_by_status = {}
#         # for status, _ in status_choices:
#         #     reservations_count = Reservation.objects.filter(statut=status).count()
#         #     reservations_by_status[status] = reservations_count
#         # average_price = Reservation.objects.aggregate(avg_price=Avg('prix_total'))['avg_price']
#         return Response({'total_reservations': total_reservations,
#                         #  'total_revenue': total_revenue,
#                         #  'reservations_by_property_type': reservations_by_type,
#                         #  'reservations_by_status': reservations_by_status,
#                         #  'average_price': average_price
#                         })
# class ReservationsByMonthYear(APIView):
#     def get(self, request):
#         reservations_by_month_year = Reservation.objects.annotate(
#             day=TruncDay('date_arrive'),
#             month=TruncMonth('date_arrive'),
#             year=TruncYear('date_arrive')
#         ).values('day','month', 'year').annotate(count=Count('id'))

#         monthly_revenue = Reservation.objects.annotate(
#             month=TruncMonth('date_arrive')
#         ).values('month').annotate(revenue=Sum('prix_total'))
        
#         annual_revenue = Reservation.objects.annotate(
#             year=TruncYear('date_arrive')
#         ).values('year').annotate(revenue=Sum('prix_total'))
#         return Response({'reservations_by_month_year': reservations_by_month_year,
#                          'monthly_revenue': monthly_revenue,
#                          'annual_revenue': annual_revenue})

# class OccupancyRate(APIView):
#     def get(self, request):
#         # Récupérer le nombre de réservations par mois/année
#         reservations_by_month_year = Reservation.objects.annotate(
#             day=TruncDay('date_arrive'),
#             month=TruncMonth('date_arrive'),
#             year=TruncYear('date_arrive')
#         ).values('day','month', 'year').annotate(count=Count('id'))

#         # Récupérer la capacité totale par mois/année
#         capacity_by_month_year = Reservation.objects.annotate(
#             month=TruncMonth('date_arrive'),
#             year=TruncYear('date_arrive')
#         ).values('month', 'year').annotate(capacity=Count('id'))

#         # Calculer le taux d'occupation
#         occupancy_rate = []
#         for res, cap in zip(reservations_by_month_year, capacity_by_month_year):
#             month = res['month']
#             year = res['year']
#             reservations = res['count']
#             capacity = cap['capacity']
#             rate = (reservations / capacity) * 100 if capacity > 0 else 0
#             occupancy_rate.append({'month': month, 'year': year, 'occupancy_rate': rate})

#         return Response({'occupancy_rate': occupancy_rate})


# class ReservationsByRegion(APIView):
#     def get(self, request):
#         regions = Bien.objects.values('region').distinct()
#         reservations_by_region = {}
#         for region in regions:
#             region_name = region['region']
#             reservations_count = Reservation.objects.filter(bien__region=region_name).count()
#             reservations_by_region[region_name] = reservations_count
#         regions = Bien.objects.values('region').distinct()
#         revenue_by_region = {}
#         for region in regions:
#             region_name = region['region']
#             region_revenue = Reservation.objects.filter(bien__region=region_name).aggregate(Sum('prix_total'))['prix_total__sum']
#             revenue_by_region[region_name] = region_revenue

#         return Response({'reservations_by_region': reservations_by_region,
#                          'revenue_by_region': revenue_by_region})

# class OccupancyRateByRegion(APIView):
#     def get(self, request):
#         regions = Bien.objects.values('region').distinct()
#         occupancy_rate_by_region = {}
#         for region in regions:
#             region_name = region['region']
            
#             # Récupérer le nombre de réservations pour la région
#             reservations_count = Reservation.objects.filter(bien__region=region_name).count()
            
#             # Récupérer la capacité totale pour la région
#             region_capacity = Bien.objects.filter(region=region_name).count()
            
#             # Calculer le taux d'occupation pour la région
#             rate = (reservations_count / region_capacity) * 100 if region_capacity > 0 else 0
#             occupancy_rate_by_region[region_name] = rate
#         return Response({'occupancy_rate_by_region': occupancy_rate_by_region})


# class OccupancyRateByPropertyType(APIView):
#     def get(self, request):
#         property_types = Bien.TYPES_CHOICES
#         occupancy_rate_by_type = {}
#         for property_type, _ in property_types:
#             # Récupérer le nombre de réservations pour ce type de bien
#             reservations_count = Reservation.objects.filter(bien__type=property_type).count()
            
#             # Récupérer la capacité totale pour ce type de bien
#             property_capacity = Bien.objects.filter(type=property_type).count()
            
#             # Calculer le taux d'occupation pour ce type de bien
#             rate = (reservations_count / property_capacity) * 100 if property_capacity > 0 else 0
#             occupancy_rate_by_type[property_type] = rate
#         return Response({'occupancy_rate_by_type': occupancy_rate_by_type})


# class OccupancyRateByPropertyStatus(APIView):
#     def get(self, request):
#         property_statuses = Bien.STATUT_CHOICES
#         occupancy_rate_by_status = {}
#         for property_status, _ in property_statuses:
#             # Récupérer le nombre de réservations pour les biens avec ce statut
#             reservations_count = Reservation.objects.filter(bien__statut=property_status).count()
            
#             # Récupérer la capacité totale pour les biens avec ce statut
#             property_capacity = Bien.objects.filter(statut=property_status).count()
            
#             # Calculer le taux d'occupation pour les biens avec ce statut
#             rate = (reservations_count / property_capacity) * 100 if property_capacity > 0 else 0
#             occupancy_rate_by_status[property_status] = rate
#         return Response({'occupancy_rate_by_status': occupancy_rate_by_status})


# class OccupancyRateByServiceType(APIView):
#     def get(self, request):
#         service_types = Service.objects.values_list('nom', flat=True)
#         occupancy_rate_by_service = {}
#         for service_type in service_types:
#             # Récupérer le nombre de réservations pour les biens avec ce type de service
#             reservations_count = Reservation.objects.filter(bien__services__nom=service_type).count()
            
#             # Récupérer la capacité totale pour les biens avec ce type de service
#             property_capacity = Bien.objects.filter(services__nom=service_type).count()
            
#             # Calculer le taux d'occupation pour les biens avec ce type de service
#             rate = (reservations_count / property_capacity) * 100 if property_capacity > 0 else 0
#             occupancy_rate_by_service[service_type] = rate
#         return Response({'occupancy_rate_by_service': occupancy_rate_by_service})
