# Generated by Django 5.0.6 on 2024-05-21 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sifreler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Sifre',
        ),
        migrations.RenameField(
            model_name='yetkili',
            old_name='CalistigiBirim',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='yetkili',
            old_name='Ad',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='yetkili',
            old_name='Soyad',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='yetkili',
            old_name='Gorev',
            new_name='specialization',
        ),
    ]
