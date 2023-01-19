# API

from rest_framework import serializers
from .models import Library, Author


class BoormagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['pk', 'name', 'number_pages', 'price', 'sizes', 'cover_type', 'date_publication']






class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name2', 'firstname', 'lastname', 'biograf','date_of_birth','date_of_death']




class EmailSerializer(serializers.Serializer):
    resipient = serializers.EmailField()
    subject = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=200)