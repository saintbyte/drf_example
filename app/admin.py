from django.contrib import admin
from .models import Appication

class AppicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Appication, AppicationAdmin)