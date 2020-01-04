from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from froala_editor.fields import FroalaField
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
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE,
                                 related_name='services', verbose_name='Специальность')
    name = models.CharField(max_length=250, verbose_name='Название услуги')
    description = FroalaField(verbose_name='Описание услуги')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена услуги')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(self.slug, ext)
        return 'images/services/{0}'.format(filename)

    image = models.ImageField(verbose_name='Фото', upload_to=get_picture_url, blank=True, null=True)
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(320, 320)],
                                 format='JPEG', options={'quality': 90})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('name',)

    def __str__(self):
        return self.name
