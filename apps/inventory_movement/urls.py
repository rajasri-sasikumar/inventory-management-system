# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'inventory_movement'

urlpatterns = [
    path(
        'api/',
        include(
            'apps.inventory_movement.api.urls',
            namespace='api'
        )
    ),
]