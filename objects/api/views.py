from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from ..models import Object
from django.http import JsonResponse

@api_view(['GET'])
def get_object_restorecount(request):
  object_type_counts = Object.objects.values('object_type').annotate(restored_count=Count('object_type'))
  data = list(object_type_counts)

    # Return the data as JSON response
  return JsonResponse(data, safe=False)
   