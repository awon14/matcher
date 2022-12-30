from . models import request_model, results_model
from rest_framework import serializers



class request_serializer(serializers.ModelSerializer):
    class Meta:
        model = request_model
        fields = '__all__'
        
        
class results_serializer(serializers.ModelSerializer):
    class Meta:
        model = results_model
        fields = '__all__'