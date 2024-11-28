from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myApp.models import Sensor
from .serializers import SensorSerializer

# Create your views here.
# GET de todos los sensores
@api_view(['GET'])
def getSensores(request):
    sensores = Sensor.objects.all()
    serializer = SensorSerializer(sensores, many=True)
    return Response(serializer.data)