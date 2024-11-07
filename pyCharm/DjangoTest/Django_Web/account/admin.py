from django.contrib import admin
from .models import account

# Register your models here.

class accountAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

admin.site.register(account, accountAdmin)