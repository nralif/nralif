from django.contrib import admin

from .models import profile
# Register your models here.

class profileAdmin(admin.ModelAdmin):

    list_display =[
        'name',
        'age',
        'address',
        'Image'
    ]

admin.site.register(profile,profileAdmin)