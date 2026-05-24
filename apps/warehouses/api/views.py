# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from apps.warehouses.models import Warehouse

from apps.warehouses.api.serializers import (
    WarehouseCreateSerializer,
    WarehouseListSerializer,
    WarehouseDetailSerializer,
    WarehouseUpdateSerializer,
)


class WarehousesViewSet(ViewSet):

    def get_queryset(self):
        return Warehouse.objects.all().order_by('-created_at')

    def list(self, request):

        queryset = self.get_queryset()

        serializer = WarehouseListSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        warehouse = get_object_or_404(
            Warehouse,
            pk=pk
        )

        serializer = WarehouseDetailSerializer(warehouse)

        return Response(serializer.data)

    def create(self, request):

        serializer = WarehouseCreateSerializer(
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

        warehouse = get_object_or_404(
            Warehouse,
            pk=pk
        )

        serializer = WarehouseUpdateSerializer(
            warehouse,
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

        warehouse = get_object_or_404(
            Warehouse,
            pk=pk
        )

        warehouse.delete()

        return Response(
            {
                'message': 'Warehouse deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )