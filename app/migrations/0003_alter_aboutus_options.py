# Generated by Django 4.1.4 on 2023-04-21 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_aboutus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'ordering': ['-id'], 'verbose_name': 'About Us', 'verbose_name_plural': "About Us's"},
        ),
    ]
