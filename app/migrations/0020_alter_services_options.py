# Generated by Django 4.1.4 on 2023-04-25 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_services_service_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['id'], 'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]
