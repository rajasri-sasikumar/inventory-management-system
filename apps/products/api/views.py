# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from apps.products.models import Product

from apps.products.api.serializers import (
    ProductCreateSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    ProductUpdateSerializer,
)


class ProductsViewSet(ViewSet):

    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')

    def list(self, request):

        queryset = self.get_queryset()

        serializer = ProductListSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        product = get_object_or_404(
            Product,
            pk=pk
        )

        serializer = ProductDetailSerializer(product)

        return Response(serializer.data)

    def create(self, request):

        serializer = ProductCreateSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):

        product = get_object_or_404(
            Product,
            pk=pk
        )

        serializer = ProductUpdateSerializer(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):

        product = get_object_or_404(
            Product,
            pk=pk
        )

        product.delete()

        return Response(
            {
                'message': 'Product deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )