# Generated by Django 5.2 on 2025-05-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_certificate_certificate_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('link', models.URLField(blank=True, default='', max_length=254, verbose_name='Link')),
                ('icon', models.CharField(blank=True, default='', max_length=254, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Medias',
                'ordering': ('link',),
            },
        ),
    ]
