from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Assistance(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    addr1 = models.TextField(max_length=100)
    addr2 = models.TextField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    assistance_needed = models.CharField(max_length=50)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class CanAssist(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    ngo_name = models.CharField(max_length=100, null=True, blank=True)
    addr = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    assistance_offer = models.CharField(max_length=50)
    city_assist = models.CharField(max_length=50)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class AcceptedOffer(models.Model):
    name = models.ForeignKey(CanAssist, on_delete=models.CASCADE)
    assistance_offer = models.CharField(max_length=50)
    accepted = models.BooleanField()

class AcceptedAssist(models.Model):
    name = models.ForeignKey(Assistance, on_delete=models.CASCADE)
    assistance_offer = models.CharField(max_length=50)
    accepted = models.BooleanField()
