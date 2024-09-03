from django.db import models

# Create your models here.
class Category (models.Model):
    cat_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    cat_img = models.ImageField(upload_to="photos/categories", blank=True)

    def str(self):
        return self.cat_name
    
class product(models.Model):
    product_name  = models.CharField(max_length=200,unique=True)
    slug          = models.SlugField(max_length=200,unique=True)
    discription   = models.CharField(max_length=500,unique=True)
    price         = models.IntegerField()
    images        = models.ImageField(upload_to='photo/products')
    stock         = models.IntegerField()
    is_available  = models.BooleanField(default=True)
    category      = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name