# Generated by Django 3.2.5 on 2021-07-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_topshiriq_ilova'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topshiriq',
            name='muddat',
            field=models.DateField(blank=True, null=True),
        ),
    ]