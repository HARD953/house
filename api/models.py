from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from custumer.models import CustomUser

class Equipement(models.Model):
    nom = models.CharField(max_length=255,primary_key=True)
    quantite=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nom
    
class Service(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return self.nom

# class Bien(models.Model):
#     owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     region =models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     numero = models.FloatField()
#     nom = models.CharField(max_length=255, blank=True, null=True)
#     nombre_chambre = models.FloatField()
#     description = models.TextField()
#     statut = models.CharField(max_length=255)
#     services = models.ManyToManyField(Service,blank=True)  # Modifiez ici pour utiliser ManyToManyField
#     etoile = models.FloatField()
#     logitude= models.DecimalField(max_digits=10, decimal_places=2)
#     latitude= models.DecimalField(max_digits=10, decimal_places=2)
#     img1 = models.ImageField(upload_to='property_images/', blank=True)
#     img2 = models.ImageField(upload_to='property_images/', blank=True)
#     img3 = models.ImageField(upload_to='property_images/', blank=True)
#     img4 = models.ImageField(upload_to='property_images/', blank=True)
#     img5 = models.ImageField(upload_to='property_images/', blank=True)
#     def __str__(self):
#         return self.nom
    
class Chambre(models.Model):
    typebien=models.CharField(max_length=255)
    nombien=models.CharField(max_length=255)
    nomchambre=models.CharField(max_length=255)
    commune=models.CharField(max_length=255)
    etoile = models.FloatField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    capacitelits = models.CharField(max_length=255)
    apropos = models.TextField()
    equipements = models.ManyToManyField(Equipement, blank=True)  # Modifiez ici pour utiliser ManyToManyField
    emplacement =models.CharField(max_length=255)
    disponibilite = models.BooleanField(default=False)
    reduction = models.CharField(max_length=255)
    img1 = models.ImageField(upload_to='property_images/', blank=True)
    img2 = models.ImageField(upload_to='property_images/', blank=True)
    img3 = models.ImageField(upload_to='property_images/', blank=True)
    img4 = models.ImageField(upload_to='property_images/', blank=True)
    img5 = models.ImageField(upload_to='property_images/', blank=True)
    def __str__(self):
        return ("{}_{}".format(self.disponibilite,self.prix))

class Reservation(models.Model):
    id_chambre=models.IntegerField()
    statut =models.CharField(max_length=255,default="En_cours")
    date_arrive = models.DateField()
    date_depart = models.DateField()
    adulte = models.DecimalField(max_digits=10, decimal_places=2)
    enfant = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2,blank=True)

    def save(self, *args, **kwargs):
        self.prix_adultes = self.adulte * 50
        self.prix_enfants = self.enfant * 25
        self.prix_total = self.prix_adultes + self.prix_enfants
        super(Reservation, self).save(*args, **kwargs)
    def __str__(self):
        return ("{}_{}".format(self.user,self.prix_total))

class Commentaire(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    comment = models.TextField()




