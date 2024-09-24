from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tour/<int:pk>/', HomeToursDetailView.as_view(), name='tour_detail'),
    path('hot-tours/', HotToursView.as_view(), name='hot_tours'),
    path('special-offers/', SpecialOffersView.as_view(), name='special_offers'),
]


