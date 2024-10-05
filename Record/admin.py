from django.contrib import admin
from .models import Recording

class RecordingAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'file')

admin.site.register(Recording, RecordingAdmin)