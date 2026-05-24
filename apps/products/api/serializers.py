# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.products.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = [
            'id',
            'sku',
            'name',
            'price',
            'quantity',
        ]


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = [
            'sku',
            'name',
            'description',
            'price',
            'quantity',
        ]


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = [
            'name',
            'description',
            'price',
            'quantity',
        ]