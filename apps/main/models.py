from django.db import models

# Create your models here.


class Cities(models.Model):
    city = models.CharField('Город',max_length=50)
    slug = models.SlugField('URL', unique=True)
    country = models.CharField('Страна',max_length=50)
    description = models.TextField('Описание')
    special_offer = models.BooleanField('Спецпредложение', default=False)
    image = models.ImageField('Изображение', upload_to='cities/')
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city


class Tours(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')
    image = models.ImageField('Изображение', upload_to='tours/')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    is_hot = models.BooleanField('Горящий тур', default=False)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.title


    

class CityTours(models.Model):
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Город тур'
        verbose_name_plural = 'Город туры'

    def __str__(self):
        return f'{self.city} {self.tour}'
    


# class SpecialOffers(models.Model):
#     country = models.CharField('Страна')
#     city = models.ForeignKey(Cities, on_delete=models.CASCADE)
#     description = models.TextField('Описание')
#     image = models.ImageField('Изображение', upload_to='offers/')

#     class Meta:
#         verbose_name = 'Спецпредложение'
#         verbose_name_plural = 'Спецпредложения'
    
#     def __str__(self):
#         return self.city.city