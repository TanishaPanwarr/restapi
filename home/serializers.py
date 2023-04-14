from dataclasses import field
from .models import Mobproduct
from .models import Mobproduct
from rest_framework import serializers
class MobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobproduct
        fields=['id','name','prize','ram','rom']
       

      
           