# Generated by Django 4.1.4 on 2023-04-28 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_frequently_asked_question_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('fax', models.PositiveIntegerField(blank=True, null=True)),
                ('location_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Contact Info',
                'verbose_name_plural': 'Contact Info',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='HeadOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('phone_number', models.PositiveIntegerField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_informations', to='app.contact_info')),
            ],
            options={
                'verbose_name': 'Head Office',
                'verbose_name_plural': 'Head Office',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('phone_number', models.PositiveIntegerField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_info', to='app.contact_info')),
            ],
            options={
                'verbose_name': 'Branch Office',
                'verbose_name_plural': 'Branch Office',
                'ordering': ['-id'],
            },
        ),
    ]