from rest_framework import serializers
from .models import *

class Application_serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields='__all__'
    
    class SerializerSelectedColumn(serializers.ModelSerializer):
        
        class Meta:
            model:Product
            fields=['product_name','product_code']