from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
# def get_url(self):
#     return reverse()


class category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

class feature_products(models.Model):
    def __str__(self):
        return self.name
    name= models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,unique=True)
    img = models.ImageField(upload_to='picture')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    prod_cat = models.ForeignKey(category,on_delete=models.CASCADE)
    pro_desc = models.CharField(max_length=1000)



# class products(models.Model):
#     def __str__(self):
#         return self.name
#     name = models.CharField(max_length=100)
#     img = models.ImageField(upload_to='picture')
#     price = models.IntegerField()
#     offer = models.BooleanField(default=False)
#     prod_cat=models.CharField(max_length=100)

