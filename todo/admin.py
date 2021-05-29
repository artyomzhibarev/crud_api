from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Note, CustomUser


@admin.register(Note)
class NoteAdmin(ModelAdmin):
    pass


@admin.register(CustomUser)
class UserAdmin(ModelAdmin):
    pass
