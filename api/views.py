from django.shortcuts import render
from django.views.generic.edit import CreateView
from rest_framework import viewsets, serializers
from .serializers import stockSerializer,cryptoSerializer
from asset_dashboard import models

# Create your views here.
class stockTracker(viewsets.ModelViewSet):
    queryset = models.stock_tracker.objects.all()
    serializer_class = stockSerializer
    
    


class cryptoTracker(viewsets.ModelViewSet):
    queryset = models.crypto_tracker.objects.all()
    serializer_class = cryptoSerializer
    