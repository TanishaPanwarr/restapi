from .models import Mobproduct
from rest_framework import viewsets
from .serializers import MobSerializer
class MobViewSet(viewsets.ModelViewSet):
    queryset=Mobproduct.objects.all()
    serializer_class=MobSerializer
    