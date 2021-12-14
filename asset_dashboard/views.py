from django.shortcuts import render
from django.views.generic.edit import CreateView
from rest_framework import generics, serializers


class dashboard(CreateView):
    template_name = 'dashboard.html'
