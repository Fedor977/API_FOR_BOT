from django.db import models
from django.utils.text import slugify
import uuid

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
    image = models.ImageField(upload_to='products/', verbose_name='Картинка')
    name = models.CharField(max_length=15, verbose_name='Имя продукта')
    description = models.TextField(max_length=200, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    slug = models.SlugField(max_length=12, unique=True, blank=True, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        if self.price < 0:
            raise ValueError("Цена не может быть меньше нуля")
        if not self.slug:
            self.slug = slugify(self.name)[:6] + "-" + str(uuid.uuid4())[:3]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
