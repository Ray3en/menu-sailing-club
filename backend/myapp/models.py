from django.db import models


class Category(models.Model):
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f'({self.id}) {self.name}'


class Subcategory(models.Model):
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f'({self.id}) {self.name}'


class Product(models.Model):
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    subcategory = models.ForeignKey(
        Subcategory, related_name='products', on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return f'({self.id}) {self.title}'
