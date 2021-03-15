from django.contrib import admin
from .models import Youtuber
# Register your models here.

class YtAdmin(admin.ModelAdmin):
    list_display = ('id',' name','subs_count','its_feature')
    search_field = ('name','camera_type')
    list_filter = ('city','camera_type')
    list_dispaly_link = ('id','name')

admin.site.register(Youtuber, YtAdmin)
