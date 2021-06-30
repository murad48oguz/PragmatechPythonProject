from django.contrib import admin
from .models import Attorney

# Register your models here.
admin.site.site_header = " This is Django Admin Panel"


class AttorneyAdmin(admin.ModelAdmin):
    list_display = ('name','date',)
    list_filter = ('date','name')
    search_fields = ['name','surname','absolutejob']
    
admin.site.register(Attorney,AttorneyAdmin)
