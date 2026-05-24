# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.inventory_movement.models import InventoryMovement


class InventoryMovementListSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    warehouse_name = serializers.CharField(
        source='warehouse.name',
        read_only=True
    )

    class Meta:
        model = InventoryMovement

        fields = [
            'id',
            'product',
            'product_name',
            'warehouse',
            'warehouse_name',
            'movement_type',
            'quantity',
            'created_at',
        ]


class InventoryMovementCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryMovement

        fields = [
            'product',
            'warehouse',
            'movement_type',
            'quantity',
            'reference_number',
            'remarks',
        ]


class InventoryMovementDetailSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    warehouse_name = serializers.CharField(
        source='warehouse.name',
        read_only=True
    )

    class Meta:
        model = InventoryMovement
        fields = '__all__'


class InventoryMovementUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryMovement

        fields = [
            'movement_type',
            'quantity',
            'reference_number',
            'remarks',
        ]