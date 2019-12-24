from django.contrib import admin
from doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id',  'last_name', 'first_name', 'patronymic', 'specialty')
    list_display_links = ('last_name',)
    prepopulated_fields = {'slug': ('last_name', 'first_name', 'patronymic')}
    filter_horizontal = ('services',)
    fieldsets = (
        (None, {
            'fields': ('last_name', 'first_name', 'patronymic', 'about', 'specialty', 'services')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_desc', 'seo_keywords'),
        }),
    )
