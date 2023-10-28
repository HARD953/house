from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from custumer.models import CustomUser

class Equipement(models.Model):
    nom = models.CharField(max_length=255)
    quantite=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nom
class Service(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return self.nom
class Image(models.Model):
    texte = models.TextField()
    image = models.ImageField(upload_to='property_images/', blank=True)

class Bien(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    region =models.CharField(max_length=255)
    images = models.ManyToManyField(Image,blank=True) 
    type = models.CharField(max_length=255)
    numero = models.FloatField()
    nom = models.CharField(max_length=255, blank=True, null=True)
    nombre_chambre = models.FloatField()
    description = models.TextField()
    statut = models.CharField(max_length=255)
    services = models.ManyToManyField(Service,blank=True)  # Modifiez ici pour utiliser ManyToManyField
    etatpropriete = models.CharField(max_length=255)
    etoile = models.FloatField()
    logitude= models.DecimalField(max_digits=10, decimal_places=2)
    latitude= models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nom
    
class Chambre(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=255)
    capacitelits = models.CharField(max_length=255)
    description = models.TextField()
    region =models.CharField(max_length=255)
    equipements = models.ManyToManyField(Equipement, blank=True)  # Modifiez ici pour utiliser ManyToManyField
    disponibilite = models.BooleanField(default=True)
    numeromaintenance = models.CharField(max_length=255)
    datedernieremaintenance = models.DateField()
    reduction = models.CharField(max_length=255)
    images = models.ManyToManyField(Image,blank=True)
    bien = models.ForeignKey('Bien', on_delete=models.CASCADE,related_name="chambres")
    def __str__(self):
        return ("{}_{}".format(self.disponibilite,self.prix))

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    region =models.CharField(max_length=255)
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

class Transaction(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return ("{}_{}".format(self.reservation,self.amount))




