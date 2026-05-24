from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apps.products.urls', namespace='products')),
    path('warehouses/', include('apps.warehouses.urls', namespace='warehouses')),
    path('inventory-movement/', include('apps.inventory_movement.urls', namespace='inventory_movement')),
]