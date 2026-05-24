# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('api/', include('apps.products.api.urls', namespace='api')),
]