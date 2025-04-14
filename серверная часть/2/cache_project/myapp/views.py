from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.core.cache import cache
import time

@cache_page(60 * 5)  # Кэшировать на 5 минут
def cached_view(request):
    time.sleep(5)  # Имитация долгой операции
    return render(request, 'myapp/cached_view.html', {'time': time.time()})
 
def low_level_cache_view(request):
    cache_key = 'my_cache_key'
    cached_data = cache.get(cache_key)

    if not cached_data:
        time.sleep(5)  # Имитация долгой операции
        cached_data = time.time()
        cache.set(cache_key, cached_data, 60 * 5)  # Кэшировать на 5 минут

    return render(request, 'myapp/low_level_cache.html', {'data': cached_data})