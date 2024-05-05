from django.urls import path
from .views import *

urlpatterns = [
    # Other URL patterns
    path('get_object_type_counts/', get_object_type_counts),
    path('object_list/<str:object_type>',object_list),
    path('get_object/<str:object_type>/<int:id>',object_detail), # will return the objects with that object type and that id 
    path('get_curr_object/<str:object_type>/<int:id>',get_curr_object), 
    path('bulk_backup/',bulk_backup),
    path('restore_by_id/<uuid:uuid>/<str:objectType>/<int:id>/',restore_by_id, name='restore_by_id'),
]
