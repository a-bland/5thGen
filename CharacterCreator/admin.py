from django.contrib import admin

from .models import Character, User, Parties


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Parties)
class CharacterAdmin(admin.ModelAdmin):
    pass
