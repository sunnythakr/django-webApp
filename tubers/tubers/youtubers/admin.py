from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YtAdmin(admin.ModelAdmin):

    # def myphoto(self,object):
    #        return format_html('<img src="{}" width="40" />.format(object.photo.url)')



    list_display = ('id','name','subs_count','is_featured')
    search_fields = ('name','camera_type')
    list_filter = ('city','camera_type')
    list_dispaly_link = ('id','name')
    list_editable = ('is_featured',)


admin.site.register(Youtuber,YtAdmin)
