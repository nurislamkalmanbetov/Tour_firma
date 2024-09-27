from django.contrib import admin
from .models import Cities, Tours, Hotels

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'slug', 'country', 'description', 'special_offer', 'image')  # Отображение полей в админке

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', 'price', 'image', 'city', 'is_hot')

@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'stars', 'image', 'city', 'street', 'price', 'review_points')


# @admin.register(CityTours)
# class CityToursAdmin(admin.ModelAdmin):
#     list_display = ('city', 'tour')
