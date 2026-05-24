# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from apps.products.api.views import ProductsViewSet


app_name = 'api'

router = DefaultRouter(
    trailing_slash=False
)

router.register(
    r'products',
    ProductsViewSet,
    basename='products'
)

urlpatterns = router.urls