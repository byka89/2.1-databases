from django.contrib import admin

from work_with_database.phones.models import Phone

# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Phone, PhoneAdmin)