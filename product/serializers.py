from rest_framework import serializers
from product.models import *
class ProductSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id',
                  'product_name',
                  'desc',
                  'sku',
                  'stock',
                  'thumbnail',
                  'category',
                  'tag',
                  'manufacturer',
                  'expiry_date',
                  'marked_price',
                  'discount',
                  'discount_price',
                  'status',
                  'absolute_url',
                  )
        read_only_fields = ("discount_price",)
    
    def get_absolute_url(self,obj):
        return obj.get_absolute_url()
        
class CategorySerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'icon',
            'absolute_url',
        )
    
    def get_absolute_url(self,obj):
        return obj.get_absolute_url()
        
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image', 'caption')