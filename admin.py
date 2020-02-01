from django.contrib import admin

# Register your models here.
from dummyapp.models import Animal, Company, Actor, Tag

admin.site.register(Animal)
admin.site.register(Company)
admin.site.register(Actor)
admin.site.register(Tag)
