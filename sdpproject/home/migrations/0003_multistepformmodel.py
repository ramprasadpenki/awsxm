# Generated by Django 3.2 on 2021-05-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiStepFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('bloodgroup', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
    ]
