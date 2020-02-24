from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Cars
from .serializers import CarsSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def add_car(request):
    if request.method == 'POST':
        if request.POST.get('maker') or request.POST.get('model') or request.POST.get('description') or request.POST.get('color') or request.POST.get('doors') or request.POST.get('lot'):
            cars=Cars()
            cars.maker = request.POST.get('maker')
            cars.model = request.POST.get('model')
            cars.description = request.POST.get('description')
            cars.color = request.POST.get('color')
            cars.doors = request.POST.get('doors')
            cars.lot = request.POST.get('lot')
            cars.save()
            
    return render(request, 'add_new_car.html', {})
            
        
def car_details(request, pk):
    if request.method == 'GET':
        car = Cars.objects.get(pk=pk)
        serializer = CarsSerializer(car)
        return JSONResponse(serializer.data)

class ListCarView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
# Create your views here.
