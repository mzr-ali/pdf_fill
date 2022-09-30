from django.contrib import admin # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from core import models
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


# admin.site.register(models.User, UserAdmin)
admin.site.register(models.ApplicationInstruction)
admin.site.register(models.Form120)
admin.site.register(models.ReceptionEmail)
admin.site.register(models.ProcedureAgreement)
admin.site.register(models.AuthorizationRequest)
admin.site.register(models.Form248)
admin.site.register(models.CheckList)
admin.site.register(models.ExceptionList)
admin.site.register(models.Form244)
