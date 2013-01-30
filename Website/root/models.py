from django.db import models
import datetime
from django.forms import ModelForm

class ServiceLevel(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Zone(models.Model):
    zip_code = models.CharField(max_length=3)
    service_level = models.ForeignKey(ServiceLevel)
    zone_number = models.CharField(max_length=3)

    def __unicode__(self):
        return "Zip code: " + self.zip_code + ", Service Level: " + self.service_level.name


class Rate(models.Model):
    weight = models.IntegerField()
    service_level = models.ForeignKey(ServiceLevel)
    zone_number = models.CharField(max_length=3)
    price = models.FloatField()

    def __unicode__(self):
        return "Weight: " + str(self.weight) + ", Service level: " + self.service_level.name + ", Zone: " + str(self.zone_number)


class Shipment(models.Model):
    date = models.DateField("Date", default=datetime.date.today)
    service_level = models.ForeignKey(ServiceLevel)
    weight = models.IntegerField()
    zone_number = models.CharField(max_length=3)
    price = models.FloatField()



class User(models.Model):
        email = models.EmailField()
        password = models.CharField(max_length=64)
        first_name = models.CharField(max_length=64)
        last_name = models.CharField(max_length=64)
        date_joined = models.DateTimeField(auto_now_add=True)
        last_login = models.DateTimeField(auto_now=True)
        admin = models.BooleanField(default=False)
        guest = models.BooleanField(default=False)
	shipments = []
        def __unicode__(self):
                return self.full_name()
        class Meta:
                db_table = 'users'
        def full_name(self):
                return self.first_name + " " + self.last_name

