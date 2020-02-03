from django.db import models
from django.db.models import CharField, IntegerField, DateTimeField, DateField


class Animal(models.Model):
    animal_name = CharField(max_length=25)
    sound = CharField(max_length=25)
    number_of_legs = IntegerField()

    def __str__(self):
        return self.animal_name


class Company(models.Model):
    name = CharField(max_length=25)
    description = CharField(max_length=25)
    founded_at = DateTimeField()
    founded_by = CharField(max_length=25)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = CharField(max_length=25)
    birth_date = DateTimeField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)

    def __str__(self):
        return self.title


class Filmmaker(models.Model):
    name = CharField(max_length=255)
    active_since = DateField(max_length=255)

    def __str__(self):
        return self.name
