# -*- coding: utf-8 -*-

from django.db import models


class Warehouse(models.Model):

    name = models.CharField(
        verbose_name='Warehouse Name',
        max_length=255
    )

    code = models.CharField(
        verbose_name='Warehouse Code',
        max_length=100,
        unique=True
    )

    location = models.CharField(
        verbose_name='Warehouse Location',
        max_length=500
    )

    capacity = models.PositiveIntegerField(
        verbose_name='Warehouse Capacity',
        default=0
    )

    is_active = models.BooleanField(
        verbose_name='Is Active',
        default=True
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
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
        ordering = ['-created_at']

    def __str__(self):
        return self.name