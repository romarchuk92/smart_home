from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length = 30, verbose_name = 'Название датчика')
    description = models.CharField(max_length = 60, verbose_name = 'Описание')
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete = models.CASCADE, related_name = 'measurements', verbose_name='Датчик id')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'