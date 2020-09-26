from django.db import models
# create your products manager here
class ProductManager(models.Manager):
    def get_featured_products(self):
        return self.get_queryset().filter(featured=True).all()
        
    def get_active_products(self):
        return self.get_queryset().filter(active=True).all()
        
    def get_product_by_id(self,id):
        try:
            product = self.get_queryset().get(pk=id)
            return product
        except Product.DoesNotExist:            
            return None

# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name='title',max_length=120)
    slug = models.SlugField(verbose_name='slug', default='abc')
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to='products/',verbose_name='image',blank=True)
    objects = ProductManager()
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    def __str__(self):
        return f"<Product-title:{self.title},description:{self.description}>"

