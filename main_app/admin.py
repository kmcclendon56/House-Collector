from django.contrib import admin
from .models import House, Location, Feature

# Register your models here.
admin.site.register(House)
admin.site.register(Location)
admin.site.register(Feature)