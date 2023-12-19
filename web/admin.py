from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date')


admin.site.register(Event, EventAdmin)
