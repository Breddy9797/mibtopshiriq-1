# Generated by Django 3.2.5 on 2021-07-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_alabala'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topshiriq',
            name='ilova',
            field=models.FileField(null=True, upload_to='Ilovalar'),
        ),
    ]