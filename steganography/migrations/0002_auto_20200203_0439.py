# Generated by Django 3.0.2 on 2020-02-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steganography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='payload',
            field=models.TextField(blank=True, default=None, help_text='Compressed payload', null=True),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='uuid',
            field=models.CharField(blank=True, default='f37c188c-1849-435e-9013-a778572abd0f', help_text='Unique uuid', max_length=40, unique=True, verbose_name='UUID'),
        ),
    ]