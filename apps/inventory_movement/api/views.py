# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from apps.inventory_movement.models import InventoryMovement

from apps.inventory_movement.api.serializers import (
    InventoryMovementCreateSerializer,
    InventoryMovementListSerializer,
    InventoryMovementDetailSerializer,
    InventoryMovementUpdateSerializer,
)


class InventoryMovementsViewSet(ViewSet):

    def get_queryset(self):
        return InventoryMovement.objects.select_related(
            'product',
            'warehouse'
        ).order_by('-created_at')

    def list(self, request):

        queryset = self.get_queryset()

        serializer = InventoryMovementListSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        inventory_movement = get_object_or_404(
            self.get_queryset(),
            pk=pk
        )

        serializer = InventoryMovementDetailSerializer(
            inventory_movement
        )

        return Response(serializer.data)

    def create(self, request):

        serializer = InventoryMovementCreateSerializer(
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

        inventory_movement = get_object_or_404(
            InventoryMovement,
            pk=pk
        )

        serializer = InventoryMovementUpdateSerializer(
            inventory_movement,
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

        inventory_movement = get_object_or_404(
            InventoryMovement,
            pk=pk
        )

        inventory_movement.delete()

        return Response(
            {
                'message': 'Inventory movement deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )