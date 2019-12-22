from django.contrib import admin
from services.models import Service, ServiceCategory


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'created', 'updated')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_desc', 'seo_keywords'),
        }),
    )


admin.site.register(ServiceCategory)
