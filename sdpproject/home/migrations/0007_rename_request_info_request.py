# Generated by Django 3.2 on 2021-05-17 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_donate_reason'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='request',
            new_name='info_request',
        ),
    ]