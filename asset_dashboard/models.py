
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class stock_tracker(models.Model):
    ASSET_EQUITES = 'Equites'
    ASSET_BONDS = 'Bbonds'
    ASSET_FUTURES = 'Futures'
    ASSET_CHOICES = [
        (ASSET_EQUITES, 'Equites'),
        (ASSET_BONDS, 'Bonds'),
        (ASSET_FUTURES, 'Futures'),
    ]

    FILL_LONG = 'Long'
    FILL_SHORT = 'Short'
    FILL_CHOICES = [
        (FILL_LONG, 'LONG'),
        (FILL_SHORT, 'SHORT'),
    ]
    
    symbol = models.CharField(max_length=5)
    quantity = models.IntegerField()
    cost_per_share = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    asset = models.CharField(max_length=10, choices=ASSET_CHOICES, default=ASSET_EQUITES) 
    long_or_short = models.CharField(max_length=10, choices=FILL_CHOICES, default=FILL_LONG) 

    def __str__(self):
        return self.symbol

class crypto_tracker(models.Model):
    ASSET_BITCOIN = 'BTC'
    ASSET_LAYER1 = 'L1'
    ASSET_LAYER2 = 'L2'
    ASSET_GAMING = 'Gaming'
    
    ASSET_CHOICES = [
        (ASSET_BITCOIN, 'BITCOIN'),
        (ASSET_LAYER1, 'LAYER1'),
        (ASSET_LAYER2, 'LAYER2'),
        (ASSET_GAMING, 'GAMING'),
    ]

    FILL_LONG = 'Long'
    FILL_SHORT = 'Short'
    FILL_CHOICES = [
        (FILL_LONG, 'LONG'),
        (FILL_SHORT, 'SHORT'),
    ]
    
    symbol = models.CharField(max_length=5)
    quantity = models.IntegerField()
    cost_per_share = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    asset = models.CharField(max_length=10, choices=ASSET_CHOICES, default=ASSET_BITCOIN) 
    long_or_short = models.CharField(max_length=10, choices=FILL_CHOICES, default=FILL_LONG) 

    def __str__(self):
        return self.symbol