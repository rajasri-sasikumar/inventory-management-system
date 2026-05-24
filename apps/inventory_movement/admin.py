# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.inventory_movement.models import InventoryMovement


@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product',
        'warehouse',
        'movement_type',
        'quantity',
        'reference_number',
        'created_at',
    )

    search_fields = (
        'product__name',
        'warehouse__name',
        'reference_number',
    )

    list_filter = (
        'movement_type',
        'created_at',
    )

    ordering = (
        '-created_at',
    )