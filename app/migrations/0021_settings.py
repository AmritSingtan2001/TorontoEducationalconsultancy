# Generated by Django 4.1.4 on 2023-04-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_services_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_keywords', models.TextField()),
                ('meta_discriptions', models.TextField()),
                ('meta_author', models.TextField()),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'settings',
                'ordering': ['-id'],
            },
        ),
    ]