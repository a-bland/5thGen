from django.contrib import admin

from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
	pass