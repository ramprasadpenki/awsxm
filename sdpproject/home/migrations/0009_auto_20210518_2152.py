# Generated by Django 3.2 on 2021-05-18 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
