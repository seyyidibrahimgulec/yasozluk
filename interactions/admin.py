from django.contrib import admin

from interactions.models import Block, Favorite, Vote, Message


admin.site.register(Vote)
admin.site.register(Block)
admin.site.register(Message)
admin.site.register(Favorite)
