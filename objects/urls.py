from django.urls import path 
from . import views

urlpatterns = [
    path('backup/<int:store_id>/<str:object_type>/', views.fetch_restore, name='backup_data'),
    path('restore/<uuid:id>/',views.retore_data),
    # Add more URL patterns as needed
]

  # restore/<id>/
    #backup/<store_id>/?object_type=''