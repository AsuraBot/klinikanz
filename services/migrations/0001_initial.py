# Generated by Django 2.2.7 on 2019-12-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена услуги')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ('name',),
            },
        ),
    ]
