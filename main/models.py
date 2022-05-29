from django.db import models


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=18)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/')

    class Meta:
        verbose_name = 'Риелторы'
        verbose_name_plural = 'Риелтор'

    def __str__(self):
        return self.name + " " + self.speciality


class Estate(models.Model):
    types_of_estates = [
        ('HOUSE', 'Дом'),
        ('FLAT', 'Квартира'),
        ('COMMERCIAL', 'Коммерческий объект'),
    ]
    types_of_deals = [
        ('RENT', 'Аренда'),
        ('BUY', 'Покупка'),
        ('SELL', 'Продажа'),
    ]
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    deposit = models.BooleanField(default=False)
    area = models.PositiveIntegerField()
    street = models.CharField(max_length=150)
    floor = models.PositiveIntegerField(default=1)
    qty_rooms = models.PositiveIntegerField(default=1)
    bedroom_num = models.PositiveIntegerField(default=1)
    main_image = models.ImageField(upload_to='estateimg/')
    bathroom = models.PositiveIntegerField(default=1)
    price = models.CharField(max_length=100, default="-")
    type_of_estate = models.CharField(max_length=20, choices=types_of_estates, default='Дом')
    type_of_deal = models.CharField(max_length=7, choices=types_of_deals, default='Продажа')

    class Meta:
        verbose_name = 'Список недвижимости'
        verbose_name_plural = 'Объект'

    def __str__(self):
        return self.title


class EstateImages(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='estateimg/')
