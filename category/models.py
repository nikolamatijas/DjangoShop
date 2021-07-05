from django.db import models

class Category(models.Model):

    category_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
