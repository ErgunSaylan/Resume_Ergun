# Generated by Django 5.2 on 2025-04-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_parameters_generalsetting_parameter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name',), 'verbose_name': 'General Setting', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=254, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='parameter',
            field=models.CharField(blank=True, default='', verbose_name='Parameter'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
