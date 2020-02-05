# External dependencies
from rest_framework import serializers

# Local dependencies, import models
from steganography.models import EmbedImage, ExtractImage

class EmbedImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmbedImage
        fields = ('uuid', 'image', 'text', 'payload')
        read_only_fields = ('uuid', 'payload')
        
class ExtractImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractImage
        fields = ('uuid', 'image', 'text', 'payload')
        read_only_fields = ('uuid', 'text', 'payload')