from rest_framework import serializers
from web.models import Event, Gallery, Contact


class ListEventSerializer(serializers.ModelSerializer):
       class Meta:
        model = Event
        fields = '__all__'


class ListGallerySerializer(serializers.ModelSerializer):
       class Meta:
        model = Gallery
        fields = '__all__'


class AddContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'