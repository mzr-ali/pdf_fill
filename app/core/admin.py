from django.contrib import admin # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from core import models
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.ApplicationInstruction)
admin.site.register(models.Form120)
