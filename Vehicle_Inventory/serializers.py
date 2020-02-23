from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cars
		fields = ("id", "maker", "model", "description", "color", "doors", "lot" )