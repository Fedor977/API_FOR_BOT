from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    image = models.ImageField(upload_to='media/', max_length=20, verbose_name='Картинка')
    name = models.CharField(max_length=15, verbose_name='Имя продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    slug = models.SlugField(max_length=9, unique=True, blank=True, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:9]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
