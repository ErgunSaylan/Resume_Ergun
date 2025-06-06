# Generated by Django 5.2 on 2025-05-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, default='', max_length=254, verbose_name='Slug')),
                ('button_text', models.CharField(blank=True, default='', max_length=254, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, default='', upload_to='documents/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('name',),
            },
        ),
    ]
