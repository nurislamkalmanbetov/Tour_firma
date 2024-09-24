from django.contrib import admin
from .models import Cities, Tours, CityTours

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city', 'slug', 'country', 'description', 'special_offer', 'image')  # Отображение полей в админке

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'price', 'image', 'city', 'is_hot')

# @admin.register(CityTours)
# class CityToursAdmin(admin.ModelAdmin):
#     list_display = ('city', 'tour')
