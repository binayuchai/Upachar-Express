from django.contrib import admin
from product.models import Product,Category,Tag,ProductImage,Manufacturer
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','thumbnail']
    
    def thumbnail_display(self,obj):
        
        if obj.thumbnail:
            return '<img src="{0}" style="max-width:100px; max-height:100px;" />'.format(obj.thumbnail.url)
        else:
            return 'No Thumbnail'
        
    thumbnail_display.allow_tags = True
    thumbnail_display.short_description = 'Thumbnail'
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ProductImage)
admin.site.register(Manufacturer)