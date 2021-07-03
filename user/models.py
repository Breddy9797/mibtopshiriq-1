from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    hodim = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bolim = models.CharField(max_length=200, null=True)
    rol = models.CharField(max_length=150, null=True)
    telefon = models.CharField(max_length=50, null=True)
    rasm = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')
    telegram_id = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.hodim.username}-Profili'