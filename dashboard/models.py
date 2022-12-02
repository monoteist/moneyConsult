from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Имя', max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Payment(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='payments')
    price = models.PositiveIntegerField('Сумма')
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
