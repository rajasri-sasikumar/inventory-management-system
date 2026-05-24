# -*- coding: utf-8 -*-

from django.db import models

from apps.products.models import Product
from apps.warehouses.models import Warehouse


class InventoryMovement(models.Model):

    MOVEMENT_TYPE_CHOICES = (
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('TRANSFER', 'Stock Transfer'),
        ('RETURN', 'Stock Return'),
    )

    product = models.ForeignKey(
        Product,
        verbose_name='Product',
        on_delete=models.CASCADE,
        related_name='inventory_movements'
    )

    warehouse = models.ForeignKey(
        Warehouse,
        verbose_name='Warehouse',
        on_delete=models.CASCADE,
        related_name='inventory_movements'
    )

    movement_type = models.CharField(
        verbose_name='Movement Type',
        max_length=50,
        choices=MOVEMENT_TYPE_CHOICES
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Movement Quantity'
    )

    reference_number = models.CharField(
        verbose_name='Reference Number',
        max_length=255,
        blank=True,
        null=True
    )

    remarks = models.TextField(
        verbose_name='Remarks',
        blank=True,
        null=True
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
        verbose_name = 'Inventory Movement'
        verbose_name_plural = 'Inventory Movements'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product.name} - {self.movement_type}'