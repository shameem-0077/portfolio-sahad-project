from django.contrib import admin

from .models import Event, Gallery, Contact


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email', 'phone_number', 'message', )

admin.site.register(Event, EventAdmin,)
admin.site.register(Gallery, GalleryAdmin,)
admin.site.register(Contact, ContactAdmin)

