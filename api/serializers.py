from django.db.models import fields
from rest_framework import serializers
from asset_dashboard.models import crypto_tracker,stock_tracker

class stockSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('symbol','quantity','cost_per_share','date','asset','long_or_short')
        model = stock_tracker

class cryptoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('symbol','quantity','cost_per_share','date','asset','long_or_short')
        model = crypto_tracker