from django.urls import path
from rest_framework import urlpatterns
from .views import stockTracker,cryptoTracker
from . import views
from rest_framework.routers import DefaultRouter

#urlpatterns = [
   # path('', stockTracker.as_view()),
    #path('stock', stockTracker.as_view()),
    #path('crypto', cryptoTracker.as_view()),
#]

router = DefaultRouter()
router.register('stock', stockTracker, basename='stock')
router.register('crypto', cryptoTracker, basename='crypto')

urlpatterns = router.urls+ [

]