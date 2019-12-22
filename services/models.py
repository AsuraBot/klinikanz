from django.db import models
from core.models import SEO


class ServiceCategory(SEO):
    name = models.CharField(max_length=250, verbose_name='Название специальности')
    description = models.TextField(verbose_name='Описание специальности')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Service(SEO):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services',
                                 verbose_name='Специальность')
    name = models.CharField(max_length=250, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услуги')          # tinymce?
    price = models.PositiveIntegerField(default=0, verbose_name='Цена услуги')
    # doctors = models.ManyToManyField(Doctor, verbose_name='Доктора', related_name='services')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('name',)

    def __str__(self):
        return self.name
