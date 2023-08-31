# Generated by Django 4.1.4 on 2023-04-21 05:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='aboutimages/')),
                ('discriptions', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'AboutUs',
                'verbose_name_plural': "AboutUs's",
                'ordering': ['-id'],
            },
        ),
    ]