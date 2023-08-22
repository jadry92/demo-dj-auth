from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from django.contrib.sessions.models import Session

class SessionAdmin(ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)