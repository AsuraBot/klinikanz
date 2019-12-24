from django.db import models


class SEO(models.Model):
    seo_desc = models.CharField(max_length=250, verbose_name='Description', blank=True, null=True)
    seo_keywords = models.CharField(max_length=250, verbose_name='Keywords', blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Slug')

    class Meta:
        abstract = True
