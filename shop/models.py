from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('prodt_cat',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='products')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    categ=models.ForeignKey(category,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.categ.slug,self.slug])


    def __str__(self):
        return '{}'.format(self.name)

