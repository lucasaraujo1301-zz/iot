from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Usuario(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField()
    user = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.cpf, self.name)

    def age(self):
        today = date.today()
        if self.birth_date:
            return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Lamp(models.Model):
    name = models.CharField(max_length=6)


class UserLamp(models.Model):
    active = models.BooleanField(default=False)
    lamp = models.ForeignKey(Lamp, related_name='lamp', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)


class Alarm(models.Model):
    time = models.TimeField(auto_now=True)
    position = models.CharField(max_length=6)
