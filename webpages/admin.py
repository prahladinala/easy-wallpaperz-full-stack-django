from django.contrib import admin
from .models import MyWallz
from django.utils.html import format_html
# Register your models here.


class WallsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'myphoto', 'category',
                    'for_what', 'is_trending']
    list_filter = ['category', 'for_what', 'is_trending']
    search_fields = ['title', 'category', 'for_what']
    list_display_links = ['id', 'title']
    list_editable = ['is_trending']

    def myphoto(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))


admin.site.register(MyWallz, WallsAdmin)
