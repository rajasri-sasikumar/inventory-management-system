# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from apps.inventory_movement.api.views import (
    InventoryMovementsViewSet
)


app_name = 'api'

router = DefaultRouter(
    trailing_slash=False
)

router.register(
    r'inventory-movements',
    InventoryMovementsViewSet,
    basename='inventory-movements'
)

urlpatterns = router.urls