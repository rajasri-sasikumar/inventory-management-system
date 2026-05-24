# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.warehouses.models import Warehouse


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'code',
        'name',
        'location',
        'capacity',
        'is_active',
        'created_at',
    )

    search_fields = (
        'code',
        'name',
        'location',
    )

    list_filter = (
        'is_active',
        'created_at',
    )

    ordering = (
        '-created_at',
    )