from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

# class SensorSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()

from measurement.models import Sensor, Measurement



class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']




class SensorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class MeasurementPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']


class SensorAllSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']