from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

class HomeView(ListView):
    model = Tours
    template_name = 'pages/home.html'
    context_object_name = 'tours'
    # last 3 
    queryset = Tours.objects.all()[:3]


class HomeToursDetailView(DetailView):
    model = Tours
    template_name = 'pages/tours_detail.html'
    context_object_name = 'tour'


class HotToursView(ListView):
    model = Tours 
    template_name = 'pages/hot_tours.html'
    context_object_name = 'tours'
    queryset = Tours.objects.filter(is_hot=True)


class SpecialOffersView(ListView):
    model = Cities 
    template_name = 'pages/special_offers.html'
    context_object_name = 'special_offers'
    queryset = Cities.objects.filter(special_offer=True)