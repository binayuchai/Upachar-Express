from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import ProductImage
from io import BytesIO
from PIL import Image
from django.core.files import File #to store files
import os
def make_thumbnail(image,size=(300,200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)
    thumb_io = BytesIO()
    img.save(thumb_io,'JPEG',quality=95)
    file_name = os.path.basename(image.name)
    thumbnail_name = f"{file_name}"
    thumbnail = File(thumb_io,name=thumbnail_name)
    return thumbnail

@receiver(post_save,sender=ProductImage)
def update_product_thumbnail(sender,instance,created,**kwargs):
    if created:   # Check if a new ProductImage instance was created
        product = instance.product
        print(product)
        if not product.thumbnail:
            product.thumbnail = make_thumbnail(instance.image)
            print("saved")
            product.save()
            