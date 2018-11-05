from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mainImage = models.ImageField(upload_to='images/main', blank = True)
    image1 = models.ImageField(upload_to='images/', blank = True)
    image2 = models.ImageField(upload_to='images/', blank = True)
    image3 = models.ImageField(upload_to='images/', blank = True)
    description = models.TextField(max_length=3000, blank = True)
    coord_lon = models.FloatField(default=0, blank = True)
    coord_lat = models.FloatField(default=0, blank = True)
    site_url = models.URLField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
        verbose_name = u'Место'
        verbose_name_plural =u'Места'
    def __str__(self):
        return self.name



