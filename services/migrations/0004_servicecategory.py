# Generated by Django 3.0.1 on 2019-12-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20191222_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_desc', models.CharField(max_length=250, verbose_name='Description')),
                ('seo_keywords', models.CharField(max_length=250, verbose_name='Keywords')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=250, verbose_name='Название специальности')),
                ('description', models.TextField(verbose_name='Описание специальности')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
                'ordering': ('name',),
            },
        ),
    ]