from .models import API
from rest_framework import viewsets, permissions
from .serializers import APISerializer

class APIViewSet(viewsets.ModelViewSet):
    queryset = API.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializers_class = APISerializer
