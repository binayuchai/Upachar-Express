from django.db import models
from django.utils.text import slugify



def product_image_path(instance,filename):
    return f"product/images/{instance.name}/{filename}"


def category_image_path(instance,filename):
    return f"product/category/icons/{instance.name}/{filename}"


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    

class Category(TimeStampModel):
    category_name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=category_image_path,blank=True)
    slug = models.SlugField(unique=True)

      

    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        
    def save(self,*args,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.category_name
    
    
class Product(TimeStampModel):
    product_name = models.CharField(max_length=255)
    desc = models.TextField(verbose_name="Description",blank=True)
    image = models.ImageField(upload_to=product_image_path,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(Category,related_name="products",on_delete=models.SET_NULL,null=True,blank=True)
    slug = models.SlugField(unique=True)

    
    
    def __str__(self):
        return self.product_name
    
    
    
        