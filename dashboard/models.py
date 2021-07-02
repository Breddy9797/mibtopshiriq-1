from django.db import models
from django.contrib.auth.models import User

TOPSHIRIQ_TURI = (
    ('Ariza', 'Ariza'),
    ('Murojat', 'Murojat'),
    ('Taklif', 'Taklif'),
    ('Aloqa xati', 'Aloqa xati'),
    ('Topshiriq', 'Topshiriq'),
)
HOLAT = (
    ('Yangi', 'Yangi'),
    ('Jarayonda', 'Jarayonda'),
    ('Bajarildi', 'Bajarildi'),
    ('Qaytarildi', 'Qaytarildi'),
)

KANAL = (
    ('Elektron', 'Elektron'),
    ('Pochta', 'Pochta'),
    ('Telefon', 'Telefon'),
    ('Og\'zaki', 'Og\'zaki'),
)
KIM_TOMONIDAN = (
    ('Markaziy apparat', 'Markaziy apparat'),
    ('Rahbariyat', 'Rahbariyat'),
    ('Fuqaro', 'Fuqaro'),
    ('Boshqa', 'Boshqa'),
)
PRIORITET = (
    ('O\'ta muhim', 'O\'ta muhim'),
    ('Muhim', 'Muhim'),
    ('Oddiy', 'Oddiy'),
)


class Topshiriq(models.Model):
    topshiriq_turi = models.CharField(max_length=50, choices=TOPSHIRIQ_TURI, null=True)
    qisqacha_mazmun = models.CharField(max_length=120, null=True)
    toliq_mazmun = models.TextField(null=True)
    holat = models.CharField(max_length=20, choices=HOLAT)
    ijrochi = models.ForeignKey(User, models.CASCADE, null=True)
    kanal = models.CharField(max_length=20, choices=KANAL)
    kim_tomonidan = models.CharField(max_length=30, choices=KIM_TOMONIDAN)
    prioritet = models.CharField(max_length=20, choices=PRIORITET)
    ilova = models.FileField(upload_to='Ilovalar')
    izoh = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    muddat = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Topshiriqlar'

    def __str__(self):
        return f'{self.qisqacha_mazmun}'

