from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40, null=True)
    document_number = models.CharField(max_length=8)
    is_member = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class VehicleType(models.Model):
    name = models.CharField(max_length=20)
    payment_per_night = models.FloatField()

    class Meta:
        verbose_name = 'Tipos de vehiculo'
        verbose_name_plural = 'Tipos de vehiculo'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    client = models.ForeignKey(Client, null=True)
    license_plate = models.CharField(max_length=8)
    vehicle_type = models.ForeignKey(VehicleType)
    is_exonerated = models.BooleanField(default=False)
    photo = models.ImageField(null=True)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    def __str__(self):
        return '{} {} / {}'.format(self.client.first_name, self.client.last_name, self.license_plate)


class Watchman(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = 'Vigilante'
        verbose_name_plural = 'Vigilantes'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Ticket(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=True)
    watchman = models.ForeignKey(Watchman, null=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(null=True)
    amount = models.FloatField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}-{}'.format(self.vehicle.license_plate, self.entry_time, self.departure_time)
