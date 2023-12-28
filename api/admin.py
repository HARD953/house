from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Equipement)
admin.site.register(Etablissement)
admin.site.register(Chambre)
admin.site.register(Commentaire)
admin.site.register(Reservation)
# admin.site.register(Transaction)
admin.site.register(Service)
# admin.site.register(Image)