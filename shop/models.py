from django.db import models
from django.utils.translation import gettext as _


class CategoryModel(models.Model):
    name = models.CharField(verbose_name=_('name'),max_length=255)
    slug = models.SlugField(verbose_name=_('slug'),max_length=255)

    created_at = models.DateTimeField(verbose_name=_('created'),auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=_('update'),auto_now=True)
    
    def __str__(self):
        return self.name

class ProductStatusType(models.IntegerChoices):
    published = 1,_('published') 
    draft = 2,_('draft') 

class ProductModel(models.Model):
    title = models.CharField(verbose_name=_('title'),max_length=255)
    slug = models.SlugField(verbose_name=_('slug'),max_length=255, blank=True,unique=True,allow_unicode=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING,verbose_name=_('category'),related_name='product_category')
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(verbose_name=_('image'),upload_to='shop/',default='shop/default.jpg/')
    
    price = models.DecimalField(verbose_name=_('price'),max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name=_('stock'),)
    status = models.IntegerField(verbose_name=_('status'),choices=ProductStatusType.choices, default=ProductStatusType.published.value)
    
    created_at = models.DateTimeField(verbose_name=_('created'),auto_now_add=True)
    update_at = models.DateTimeField(verbose_name=_('update'),auto_now=True)
    
    def __str__(self):
        return self.title