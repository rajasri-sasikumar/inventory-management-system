# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'sku',
        'name',
        'price',
        'quantity',
        'created_at',
    )

    search_fields = (
        'sku',
        'name',
    )

    list_filter = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )