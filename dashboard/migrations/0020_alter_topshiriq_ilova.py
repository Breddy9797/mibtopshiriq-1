# Generated by Django 3.2.5 on 2021-07-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_alter_topshiriq_ilova'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topshiriq',
            name='ilova',
            field=models.ImageField(blank=True, null=True, upload_to='Ilovalar'),
        ),
    ]
