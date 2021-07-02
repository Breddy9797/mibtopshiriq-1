# Generated by Django 3.2.5 on 2021-07-02 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topshiriq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topshiriq_turi', models.CharField(choices=[('Ariza', 'Ariza'), ('Murojat', 'Murojat'), ('Taklif', 'Taklif'), ('Aloqa xati', 'Aloqa xati'), ('Topshiriq', 'Topshiriq')], max_length=50, null=True)),
                ('qisqacha_mazmun', models.CharField(max_length=120, null=True)),
                ('toliq_mazmun', models.TextField(null=True)),
                ('holat', models.CharField(choices=[('Yangi', 'Yangi'), ('Jarayonda', 'Jarayonda'), ('Bajarildi', 'Bajarildi'), ('Qaytarildi', 'Qaytarildi')], max_length=20)),
                ('kanal', models.CharField(choices=[('Elektron', 'Elektron'), ('Pochta', 'Pochta'), ('Telefon', 'Telefon'), ("Og'zaki", "Og'zaki")], max_length=20)),
                ('kim_tomonidan', models.CharField(choices=[('Markaziy apparat', 'Markaziy apparat'), ('Rahbariyat', 'Rahbariyat'), ('Fuqaro', 'Fuqaro'), ('Boshqa', 'Boshqa')], max_length=30)),
                ('prioritet', models.CharField(choices=[("O'ta muhim", "O'ta muhim"), ('Muhim', 'Muhim'), ('Oddiy', 'Oddiy')], max_length=20)),
                ('ilova', models.FileField(upload_to='Ilovalar')),
                ('izoh', models.TextField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('muddat', models.DateTimeField(blank=True, null=True)),
                ('ijrochi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
