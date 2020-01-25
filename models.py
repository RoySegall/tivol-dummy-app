from django.db import models
from django.db.models import CharField, IntegerField, DateTimeField


class Animal(models.Model):
    animal_name = CharField(max_length=25)
    sound = CharField(max_length=25)
    number_of_legs = IntegerField()


class Company(models.Model):
    name = CharField(max_length=25)
    description = CharField(max_length=25)
    founded_at = DateTimeField()
    founded_by = CharField(max_length=25)
