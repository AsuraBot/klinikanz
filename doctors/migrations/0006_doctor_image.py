# Generated by Django 3.0.1 on 2019-12-25 13:47

from django.db import migrations, models
import doctors.models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_auto_20191224_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=doctors.models.Doctor.get_picture_url, verbose_name='Фото'),
        ),
    ]
