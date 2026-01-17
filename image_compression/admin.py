from django.contrib import admin
from .models import CompressImage
from django.utils.html import format_html

class CompressImageAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" style="border-radius:4px;" width="40" height="40">', obj.compressed_img.url)
    
    def org_img_size(self, obj):
        size_mb = obj.original_img.size / (1024 * 1024)
        return format_html('{} MB', f'{size_mb:.2f}')
    
    def comp_img_size(self, obj):
        size_mb = obj.compressed_img.size / (1024 * 1024)
        if size_mb > 1:
            return format_html('{} MB', f'{size_mb:.2f}')
        else:
            size_kb = obj.compressed_img.size / 1024
            return format_html('{} KB', f'{size_kb:.2f}')


    def compression_percentage(self, obj):
        return obj.quality


    list_display = ['user', 'thumbnail', 'org_img_size', 'comp_img_size', 'compression_percentage', 'compressed_at']

admin.site.register(CompressImage,CompressImageAdmin)
