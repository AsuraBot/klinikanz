from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from froala_editor.fields import FroalaField
from core.models import SEO
from services.models import Service


class Doctor(SEO):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    about = FroalaField(verbose_name='Информация')
    services = models.ManyToManyField(Service, verbose_name='Услуги', related_name='doctors')
    specialty = models.CharField(max_length=250, verbose_name='Специальность')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        # slug_name = '_'.join(slugify(item) for item in (self.last_name, self.first_name, self.patronymic))
        filename = '{0}.{1}'.format(self.slug, ext)
        return 'images/doctors/{0}'.format(filename)

    image = models.ImageField(verbose_name='Фото', upload_to=get_picture_url, blank=True, null=True)
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(320, 320)],
                                 format='JPEG', options={'quality': 90})

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return '{0} {1} {2} ({3})'.format(self.last_name, self.first_name, self.patronymic, self.specialty)

    def get_full_name(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.patronymic)

    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self.last_name, str(self.first_name)[0], str(self.patronymic)[0])
