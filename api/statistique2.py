from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.db.models import*
from django.db.models.functions import*

class TotalReservations(APIView):
    def get(self, request):
        total_reservations = Reservation.objects.count()
        reservations_by_month_year = Reservation.objects.annotate(
            month=TruncMonth('date_arrive'),
            year=TruncYear('date_arrive')
        ).values('month', 'year').annotate(count=Count('id'))
        regions = Bien.objects.values('region').distinct()
        reservations_by_region = {}
        revenue_by_region = {}
        for region in regions:
            region_name = region['region']
            reservations_count = Reservation.objects.filter(chambre__region=region_name).count()
            revenue = Reservation.objects.filter(chambre__region=region_name).aggregate(Sum('prix_total'))['prix_total__sum']
            reservations_by_region[region_name] = reservations_count
            revenue_by_region[region_name] = revenue
        # 1111111111111111111111111111
        # service_types = Service.objects.values_list('nom', flat=True).distinct()
        # reservations_by_service_type = {}
        # for service_type in service_types:
        #     reservations_by_month_year = Reservation.objects.filter(bien__services__nom=service_type).annotate(
        #         month=TruncMonth('date_arrive'),
        #         year=TruncYear('date_arrive')
        #     ).values('month', 'year').annotate(count=Count('id'))
        #     reservations_by_service_type[service_type] = reservations_by_month_year
        # # 111111111111111111111111111
        # property_statuses = Bien.objects.values_list('statut', flat=True).distinct()
        # reservations_by_property_status = {}
        # for property_status in property_statuses:
        #     reservations_by_month_year = Reservation.objects.filter(bien__statut=property_status).annotate(
        #         month=TruncMonth('date_arrive'),
        #         year=TruncYear('date_arrive')
        #     ).values('month', 'year').annotate(count=Count('id'))
        #     reservations_by_property_status[property_status] = reservations_by_month_year

        return Response({'total_reservations': total_reservations,
                         'reservations_by_month_year': reservations_by_month_year,
                         'reservations_by_region': reservations_by_region,
                         'revenue_by_region': revenue_by_region,
                        #  'reservations_by_service_type': reservations_by_service_type,
                        #  'reservations_by_property_status': reservations_by_property_status
                         })
    


class OccupancyRate(APIView):
    def get(self, request):
        # Récupérer le nombre de réservations par mois/année
        reservations_by_month_year = Reservation.objects.annotate(
            month=TruncMonth('date_arrive'),
            year=TruncYear('date_arrive')
        ).values('month', 'year').annotate(count=Count('id'))

        # Récupérer la capacité totale par mois/année
        capacity_by_month_year = Reservation.objects.annotate(
            month=TruncMonth('date_arrive'),
            year=TruncYear('date_arrive')
        ).values('month', 'year').annotate(capacity=Count('id'))

        # Calculer le taux d'occupation
        occupancy_rate = []
        for res, cap in zip(reservations_by_month_year, capacity_by_month_year):
            month = res['month']
            year = res['year']
            reservations = res['count']
            capacity = cap['capacity']
            rate = (reservations / capacity) * 100 if capacity > 0 else 0
            occupancy_rate.append({'month': month, 'year': year, 'occupancy_rate': rate})
        # 11111111111111111111111111111111111
        property_types = Bien.objects.values_list('type', flat=True).distinct()
        occupancy_rate_by_type = {}
        for property_type in property_types:
            reservations_count = Reservation.objects.filter(bien__type=property_type).count()
            property_capacity = Bien.objects.filter(type=property_type).count()
            rate = (reservations_count / property_capacity) * 100 if property_capacity > 0 else 0
            occupancy_rate_by_type[property_type] = rate
        # 111111111111111111111111111111111111
        property_statuses = Bien.objects.values_list('statut', flat=True).distinct()
        occupancy_rate_by_status = {}
        for property_status in property_statuses:
            reservations_count = Reservation.objects.filter(bien__statut=property_status).count()
            property_capacity = Bien.objects.filter(statut=property_status).count()
            rate = (reservations_count / property_capacity) * 100 if property_capacity > 0 else 0
            occupancy_rate_by_status[property_status] = rate
        # 11111111111111111111111111111111111111
        service_types = Service.objects.values_list('nom', flat=True).distinct()
        occupancy_rate_by_service = {}
        for service_type in service_types:
            reservations_count = Reservation.objects.filter(bien__services__nom=service_type).count()
            property_capacity = Bien.objects.filter(services__nom=service_type).count()
            rate = (reservations_count / property_capacity) * 100 if property_capacity > 0 else 0
            occupancy_rate_by_service[service_type] = rate

        return Response({'occupancy_rate': occupancy_rate,
                         'occupancy_rate_by_type': occupancy_rate_by_type,
                         'occupancy_rate_by_status': occupancy_rate_by_status,
                         'occupancy_rate_by_service': occupancy_rate_by_service})
