from django.db import models
from django.core.validators import MaxValueValidator
from froala_editor.fields import FroalaField


class Review(models.Model):
    author = models.CharField(max_length=250, verbose_name='Автор')
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9)], verbose_name='Оценка')
    text = FroalaField(verbose_name='Отзыв')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')
    is_active = models.BooleanField(default=False, verbose_name='Показать на сайте')
    answer = FroalaField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('created',)

    def __str__(self):
        return '{0} {1}'.format(self.author, self.created)
