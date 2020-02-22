from django.shortcuts import render
from rest_framework import generics
from .models import Cars
from .serializers import CarsSerializer

def hello_world(request):
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
            return render(request, 'hello_world.html', {})
            
    return render(request, 'hello_world.html', {})
            
        
def car_detail(request, pk):
    try:
        car = Cars.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return HttpResponse(status=404) 
        
    if request.method == 'GET':
        serializer = CarsSerializer(car)
        return serializer.data

class ListCarView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
# Create your views here.
