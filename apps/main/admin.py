from django.contrib import admin
from .models import Cities, Tours, CityTours

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'description')  # Отображение полей в админке
    fields = ['city', 'slug', 'country', 'description']  # Убедитесь, что 'id' не используется

@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'price', 'image', 'city', 'is_hot')

# @admin.register(CityTours)
# class CityToursAdmin(admin.ModelAdmin):
#     list_display = ('city', 'tour')
