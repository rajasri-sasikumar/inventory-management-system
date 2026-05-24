# -*- coding: utf-8 -*-

from django.db import models


class Product(models.Model):

    sku = models.CharField(
        verbose_name='SKU',
        max_length=255,
        unique=True
    )

    name = models.CharField(
        verbose_name='Product Name',
        max_length=255
    )

    description = models.TextField(
        verbose_name='Product Description',
        blank=True,
        null=True
    )

    price = models.DecimalField(
        verbose_name='Product Price',
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Available Quantity',
        default=0
    )

    created_at = models.DateTimeField(
        verbose_name='Created At',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Updated At',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name