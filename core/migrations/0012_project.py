# Generated by Django 5.2 on 2025-05-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_sumary_name_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('Project_name', models.CharField(blank=True, default='', max_length=254, verbose_name='Project')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('parameter', models.CharField(blank=True, default='', verbose_name='Parameter')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
