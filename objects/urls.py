from django.urls import path 
from . import views

urlpatterns = [
    path('backup/<str:object_type>/', views.fetch_restore, name='backup_data'),
    path('backup_id/<str:object_type>/<int:id>', views.fetch_restore_id, name='backup_data'),
    path('restore/<uuid:id>/',views.retore_data),
    # Add more URL patterns as needed
]

  # restore/<id>/
    #backup/<store_id>/?object_type=''