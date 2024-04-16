from django.urls import path
from .views import *

urlpatterns = [
    # Other URL patterns
    path('get_object_type_counts/', get_object_type_counts),
    path('object_list/<str:object_type>',object_list)
]
