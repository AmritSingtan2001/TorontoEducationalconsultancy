# Generated by Django 4.1.4 on 2023-04-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_ourteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='image',
            field=models.ImageField(default=1, upload_to='teamimage/'),
            preserve_default=False,
        ),
    ]
