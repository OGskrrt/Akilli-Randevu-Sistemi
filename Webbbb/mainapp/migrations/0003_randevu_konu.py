# Generated by Django 5.0.6 on 2024-05-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_sifreler_delete_sifre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='randevu',
            name='Konu',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]