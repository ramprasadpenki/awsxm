# Generated by Django 3.2 on 2021-05-16 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_donate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='reason',
        ),
    ]