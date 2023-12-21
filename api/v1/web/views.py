from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.v1.web.serializers import ListEventSerializer, ListGallerySerializer

from web.models import Event, Gallery



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def list_events(request):
    instances = Event.objects.all()

    if instances.exists():
        serializer = ListEventSerializer(instance=instances, many=True, context={"request": request}).data

        response_data = {
            "status_code": 6000,
            "title": "Success",
            "data": serializer
        }
    else:
        response_data = {
            "status_code": 6001,
            "title": "Failed",
            "message": "No data found"
        }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def list_gallery(request):
    instances = Gallery.objects.all()

    if instances.exists():
        serializer = ListGallerySerializer(instance=instances, many=True, context={"request": request}).data

        response_data = {
            "status_code": 6000,
            "title": "Success",
            "data": serializer
        }
    else:
        response_data = {
            "status_code": 6001,
            "title": "Failed",
            "message": "No data found"
        }
    
    return Response(response_data, status=status.HTTP_200_OK)