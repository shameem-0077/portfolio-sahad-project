from django.contrib import admin

from .models import Event, Gallery


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image',)


admin.site.register(Event, EventAdmin,)
admin.site.register(Gallery, GalleryAdmin,)
