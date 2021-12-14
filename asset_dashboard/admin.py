from django.contrib import admin


from django.contrib import admin

from .models import  crypto_tracker,stock_tracker

admin.site.register(stock_tracker)
admin.site.register(crypto_tracker)