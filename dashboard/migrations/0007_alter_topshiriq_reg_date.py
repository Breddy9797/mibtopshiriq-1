# Generated by Django 3.2.5 on 2021-07-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_topshiriq_muddat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topshiriq',
            name='reg_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]