# Generated by Django 5.2 on 2025-05-04 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_document'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('order',), 'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
    ]
