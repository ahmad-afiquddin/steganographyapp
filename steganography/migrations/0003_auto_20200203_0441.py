# Generated by Django 3.0.2 on 2020-02-03 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steganography', '0002_auto_20200203_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='uuid',
            field=models.CharField(blank=True, default='e7c48e09-ca9a-4699-9239-922e2b4c5e9d', help_text='Unique uuid', max_length=40, unique=True, verbose_name='UUID'),
        ),
    ]