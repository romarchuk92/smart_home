# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorUpdateSerializer, SensorAllSerializer, MeasurementPostSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, UpdateAPIView

# from django.http import HttpResponse



# @api_view(['GET', 'POST'])
# def demo (request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         res = SensorSerializer(sensors, many=True)
#         # data = {'message': 'hello'}
#         return Response(res.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})



# class DemoView(APIView):
#     def get(self, requests):
#         sensors = Sensor.objects.all()
#         res = SensorSerializer(sensors, many=True)
#         # data = {'message': 'hello'}
#         return Response(res.data)  
#     def post(self, requests):
#         return Response({'status': 'OK'})


# class DemoView(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#     def post(self, requests):

#         return Response({'status': 'OK'})
    

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorAllView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorAllSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementPostSerializer

