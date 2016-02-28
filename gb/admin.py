from django.contrib import admin
from gb.models import record

# Register your models here.
class record_admin(admin.ModelAdmin):
    list_display = ('title', 'text', 'record_date')

admin.site.register(record, record_admin)
