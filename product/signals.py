from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import ProductImage

@receiver(post_save,sender=ProductImage)
def update_product_thumbnail(sender,instance,created,**kwargs):
    if created:   # Check if a new ProductImage instance was created
        product = instance.product
        print(product)
        if not product.thumbnail:
            product.thumbnail = instance.image
            print("saved")
            product.save()
            