from django.contrib import admin

# Register your models here.
from dummyapp.models import Animal, Company

admin.site.register(Animal)
admin.site.register(Company)
