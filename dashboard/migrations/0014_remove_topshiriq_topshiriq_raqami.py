# Generated by Django 3.2.5 on 2021-07-05 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_topshiriq_ilova'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topshiriq',
            name='topshiriq_raqami',
        ),
    ]