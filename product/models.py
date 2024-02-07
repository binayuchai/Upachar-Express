from django.db import models
from django.utils.text import slugify
from django.core.files import File #to store files
from django.urls import reverse

from io import BytesIO
from PIL import Image

def product_image_path(instance,filename):
    return f"product/images/{instance.product.product_name}/{filename}"


def category_image_path(instance,filename):
    return f"product/category/icons/{instance.name}/{filename}"

def compress_image(image):
    img = Image.open(image)
    img_io = BytesIO()  # Create a BytesIO object to store the compressed image
    img.save(img_io, format='JPEG', quality=70)  # Save the compressed image as JPEG format with quality 70
    new_image = File(img_io, name=image.name)    
    return new_image   


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    

class Category(TimeStampModel):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=category_image_path,blank=True)
    slug = models.SlugField(unique=True,blank=True)

      
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ('name',)
        
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
    
    
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return f'/{self.slug}/'
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

    
    

class Tag(TimeStampModel):
    name = models.CharField(max_length=100,unique=True)
  
    def __str__(self):
        return self.name
   

class Manufacturer(TimeStampModel):
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name    
     

class Status(models.TextChoices):
    DRAFT = "draft", "DRAFT"
    PUBLISH = "publish", "PUBLISH"
    BLOCKED = "blocked", "BLOCKED"
    
    
class Product(TimeStampModel):
    product_name = models.CharField(max_length=255)
    desc = models.TextField(verbose_name="Description",blank=True)
    # image = models.ImageField(upload_to=product_image_path,blank=True)
    # quantity = models.IntegerField(default=1)
    sku = models.CharField(max_length=255,unique=True)
    stock = models.PositiveBigIntegerField(default=1)
    thumbnail = models.ImageField(upload_to='product/images/product_thumbnails/', null=True, blank=True)
    category = models.ForeignKey(Category,related_name="products",on_delete=models.SET_NULL,null=True,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    tag = models.ManyToManyField(Tag)
    
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.SET_NULL,null=True,blank=True)
    expiry_date = models.DateField(verbose_name="Expiry Date")
    # rating = models.FloatField(null=True,blank=True)
    marked_price = models.DecimalField(decimal_places=2,max_digits=10)
    discount = models.DecimalField(max_digits=4,decimal_places=2,default=0.00)
    discount_price = models.DecimalField(verbose_name="Discounted Price",max_digits=10,decimal_places=2)
    status = models.CharField(max_length=100,choices=Status.choices,default=Status.DRAFT)
    
    

    
    
    def __str__(self):
        return self.product_name
    
    
    
    

    def save(self, *args, **kwargs):
        mp = self.marked_price
        dis = self.discount
        self.discount_price = mp - (dis/100 * mp)
        self.slug = slugify(self.product_name)
        
        if self.thumbnail:
            compress_image_thumbnail = compress_image(self.thumbnail)
            self.thumbnail = compress_image_thumbnail
            
        # if not self.thumbnail and self.product_images.exists():
        #     first_image = self.product_images.first()
        #     self.thumbnail = first_image.image

        super().save(*args,**kwargs)    
    
    # def get_absolute_url(self):
    #     return f'/{self.category.slug}/{self.slug}/' 
         
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})

                     
    
    
class ProductImage(TimeStampModel):
    product=models.ForeignKey(Product,related_name="product_images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path,blank=True)
    caption = models.CharField(max_length=255, blank=True)
    
    
    def save(self,*args,**kwargs):
        if self.image:
            compressed_img_io = compress_image(self.image)
            self.image = compressed_img_io
        super().save(*args, **kwargs)
    
    
        



