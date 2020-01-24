from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField


class Animal(models.Model):
    animal_name = CharField(max_length=25)
    sound = CharField(max_length=25)
    number_of_legs = IntegerField()
