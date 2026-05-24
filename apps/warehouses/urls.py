# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'warehouses'

urlpatterns = [
    path(
        'api/',
        include(
            'apps.warehouses.api.urls',
            namespace='api'
        )
    ),
]