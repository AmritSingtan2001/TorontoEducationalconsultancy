# Generated by Django 4.1.4 on 2023-04-21 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_aboutus_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'ordering': ['-id'], 'verbose_name': 'About Us', 'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'ordering': ['id'], 'verbose_name': 'Slider Image', 'verbose_name_plural': 'Slider Images'},
        ),
    ]