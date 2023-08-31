# Generated by Django 4.1.4 on 2023-04-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_services'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['-id'], 'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.RemoveField(
            model_name='services',
            name='service_slug',
        ),
        migrations.AlterField(
            model_name='services',
            name='discriptions',
            field=models.TextField(),
        ),
    ]