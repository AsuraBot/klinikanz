# Generated by Django 3.0.1 on 2019-12-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_doctor_specialty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name': 'Доктор', 'verbose_name_plural': 'Доктора'},
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(default='salam', max_length=50, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(default='epta', max_length=50, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='patronymic',
            field=models.CharField(default='12312', max_length=50, verbose_name='Отчество'),
            preserve_default=False,
        ),
    ]
