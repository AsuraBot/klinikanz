from django.db import models


class SEO(models.Model):
    seo_desc = models.CharField(max_length=250, verbose_name='Description')
    seo_keywords = models.CharField(max_length=250, verbose_name='Keywords')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Slug')

    class Meta:
        abstract = True
