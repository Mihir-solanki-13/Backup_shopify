from django.urls import path
from .views import get_object_restorecount

urlpatterns = [
    # Other URL patterns
    path('get_object_restorecount/', get_object_restorecount, name='get_object_restorecount'),
]
