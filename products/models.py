import os

# import random

from django.db import models
from django.db.models import Q  # we will use Q to give the possibility to search in content

# Create your models here.
from categories.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_galleries_image_path(instance, filename):
    # new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


# to manage products view in site for example disable showing of non-active products we use the following class
# this class must be defined before Product class
class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)  # here you can see how to get access to the objects in database

    def get_products_by_category(self, category_name):  # we use this method to filter products by their categories
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        return self.get_queryset().filter(lookup, active=True).distinct()
        # Note that, lookup must be the first parameter
        # distinct is used to prevent repeated search results to be shown
        # we can do this line in views.py, too


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')

    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # we will use this method for products detail view in products list view
        print("yes")
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_galleries_image_path, null=True, blank=True, verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'گالری محصول'
        verbose_name_plural = 'گالری های محصول'

    def __str__(self):
        return self.title
