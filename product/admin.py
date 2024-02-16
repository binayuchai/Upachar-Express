from django.contrib import admin
from product.models import Product,Category,Tag,ProductImage,Manufacturer
# from imagekit.admin import AdminThumbnail
from django.utils.html import format_html
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    
    def thumbnail_display(self,obj):
        
        if obj.thumbnail:
            print(obj.thumbnail.url)
            return format_html(f'<img src="{obj.thumbnail.url}" style="max-width:100px; max-height:100px;" />')
        
        else:
            return format_html('No Thumbnail')
        
    thumbnail_display.allow_tags = True
    thumbnail_display.short_description = 'Thumbnail'
    list_display = ['product_name','thumbnail_display']
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag)
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    
    def image_tag(self,obj):
        if obj and obj.image:
            print(obj.image.url)
            return format_html(f'<img src="{obj.image.url}" width="250" height="200" />')
        else:
            return format_html('No image')
        
    list_display = ('product','image_tag','caption')

admin.site.register(Manufacturer)