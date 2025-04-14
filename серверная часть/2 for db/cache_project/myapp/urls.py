from django.urls import path
from .views import low_level_cache_view, cached_view
urlpatterns =[
    path('cached/', cached_view, name='cached_view'),
    path('low-level-cache/', low_level_cache_view, name='low_level_cache')
]