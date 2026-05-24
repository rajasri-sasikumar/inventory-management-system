# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.warehouses.models import Warehouse


class WarehouseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse

        fields = [
            'id',
            'code',
            'name',
            'location',
            'capacity',
            'is_active',
        ]


class WarehouseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse

        fields = [
            'name',
            'code',
            'location',
            'capacity',
            'is_active',
        ]


class WarehouseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse

        fields = [
            'name',
            'location',
            'capacity',
            'is_active',
        ]