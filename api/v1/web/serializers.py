from rest_framework import serializers
from web.models import Event, Gallery


class ListEventSerializer(serializers.ModelSerializer):
       class Meta:
        model = Event
        fields = '__all__'


class ListGallerySerializer(serializers.ModelSerializer):
       class Meta:
        model = Gallery
        fields = '__all__'