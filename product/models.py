from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    icon = models.CharField(max_length=30, null=True, blank=True)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  # parent uzigz uzi ulandi

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    CHOICES = (
        (1, "new"),
        (2, "old"),
    )

    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Moderation'),
        (3, 'Sold'),
        (4, 'Inactive'),
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    discount = models.IntegerField(null=True, blank=True)
    condition = models.SmallIntegerField(choices=CHOICES)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', null=True)
    detail_image = models.ImageField(upload_to='product_detail/', null=True)

    def __str__(self):
        return "%s - %s" % (self.id, self.product)   # str ni shu tarzda formatlasa ham buladi


