from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

"""The category model will give our products a category like clothing, kitchen and dining or deals
Which will inherit from models.Model"""


class Category(models.Model):

    """To fix the spelling issue"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """on_delete=models.SET_NULL means if a category is deleted well set any products that use it
    to have null for this field rather than deleting the product"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    decription_title = models.TextField()
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    how_to_use = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # Calculates the average rating for each product
    def averagereview(self):
        ratings = Review.objects.filter(product=self).aggregate(average=Avg('rate'))
        avg = 0
        if ratings["average"] is not None:
            avg = float(ratings["average"])
        return avg

    """ Each products requires a name, description and price everything else is optional """

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=60, null=False, blank=False)
    review = models.TextField(null=False, blank=False)
    RATING_CHOICES = (
        (0, 'No rating'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rate = models.IntegerField(choices=RATING_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
