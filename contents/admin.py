from django.contrib import admin

from contents.models import Channel, Topic, Entry


admin.site.register(Channel)
admin.site.register(Topic)
admin.site.register(Entry)
