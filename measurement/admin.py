from django.contrib import admin
from .models import Sensor, Measurement
# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'name', 'description']

@admin.register(Measurement)
class SensorAdmin(admin.ModelAdmin):
    # pass
    list_display = ['sensor', 'temperature', 'created_at']