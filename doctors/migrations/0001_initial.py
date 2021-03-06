# Generated by Django 3.0.1 on 2019-12-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_desc', models.CharField(max_length=250, verbose_name='Description')),
                ('seo_keywords', models.CharField(max_length=250, verbose_name='Keywords')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=250, verbose_name='Ф.И.О. доктора')),
                ('about', models.TextField(verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Доктора',
                'ordering': ('name',),
            },
        ),
    ]
