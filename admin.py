from django.contrib import admin
from .models import *

class ShowRegister(admin.ModelAdmin):
    fields = ['show_name', 'description', 'time_slot_from', 'time_slot_to', 'audio_files', 'image', 'email']
    
class HeaderRegister(admin.ModelAdmin):
    fields = ['image']

class AudioRegister(admin.ModelAdmin):
    fields = ['audio_file', 'episode']

class NewsRegister(admin.ModelAdmin):
    fields = ['title', 'text', 'number']

admin.site.register(AudioFiles, AudioRegister)
admin.site.register(Show, ShowRegister)
admin.site.register(Header, HeaderRegister)
admin.site.register(News, NewsRegister)
