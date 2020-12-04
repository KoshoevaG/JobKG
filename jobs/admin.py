from django.contrib import admin

from .models import Category, Job, JobImage


class ImageInline(admin.TabularInline):
    model = JobImage
    extra = 0
    fields = ('image', )


class JobAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')




admin.site.register(Category)
admin.site.register(Job, JobAdmin)
admin.site.register(JobImage)