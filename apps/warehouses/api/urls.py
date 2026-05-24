# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from apps.warehouses.api.views import WarehousesViewSet


app_name = 'api'

router = DefaultRouter(
    trailing_slash=False
)

router.register(
    r'warehouses',
    WarehousesViewSet,
    basename='warehouses'
)

urlpatterns = router.urls