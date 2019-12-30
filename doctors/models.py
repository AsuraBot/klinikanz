from django.db import models
from core.models import SEO
from services.models import Service


class Doctor(SEO):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    about = models.TextField(verbose_name='Информация')
    services = models.ManyToManyField(Service, verbose_name='Услуги', related_name='doctors')
    specialty = models.CharField(max_length=250, verbose_name='Специальность')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/doctors/%s' % filename

    image = models.ImageField(verbose_name='Фото', upload_to=get_picture_url, blank=True, null=True)

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return '{0} {1} {2} ({3})'.format(self.last_name, self.first_name, self.patronymic, self.specialty)

    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self.last_name, str(self.first_name)[0], str(self.patronymic)[0])
