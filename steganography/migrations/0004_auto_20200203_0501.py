# Generated by Django 3.0.2 on 2020-02-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steganography', '0003_auto_20200203_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(blank=True, default=None, help_text='Carrier', null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='uuid',
            field=models.CharField(blank=True, default='5488c362-0c16-4862-9f75-7e44258044be', help_text='Unique uuid', max_length=40, unique=True, verbose_name='UUID'),
        ),
    ]