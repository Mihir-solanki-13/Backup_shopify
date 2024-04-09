from django.urls import path
from . import views

urlpatterns = [
    path('backup/<str:object_type>/', views.fetch_restore, name='backup_data'),
    path('backup/<str:object_type>/<int:id>/', views.fetch_restore_id, name='backup_data'),
    path('restore/<uuid:id>/',views.retore_data),
    # Add more URL patterns as needed
]

  # restore/<id>/
    #backup/<store_id>/?object_type=''
#
# from django.urls import path, include
# from rest_framework import routers
# from .views import StoreViewSet, ObjectViewSet
#
# router = routers.DefaultRouter()
# router.register(r'stores', StoreViewSet)
# router.register(r'objects', ObjectViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]