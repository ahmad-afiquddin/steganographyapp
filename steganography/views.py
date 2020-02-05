# External dependencies
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

# Local dependencies, import serializers
from steganography.serializers import EmbedImageSerializer, ExtractImageSerializer
# import models
from steganography.models import EmbedImage, ExtractImage

class EmbedImageCreateView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = EmbedImage.objects.all()
    serializer_class = EmbedImageSerializer

    def perform_create(self, serializer):
        serializer.save()

class ExtractImageCreateView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = ExtractImage.objects.all()
    serializer_class = ExtractImageSerializer

    def perform_create(self, serializer):
        serializer.save()

class EmbedDetailsView(APIView):
    model = EmbedImage
    serializer = EmbedImageSerializer

    def get_object(self, resource_uuid):
        return get_object_or_404(self.model, uuid=resource_uuid)

    def get(self, request, resource_uuid, format=None):
        instance = self.get_object(resource_uuid)
        serializer = self.serializer(instance)
        return Response(serializer.data)

class ExtractDetailsView(APIView):
    model = ExtractImage
    serializer = EmbedImageSerializer

    def get_object(self, resource_uuid):
        return get_object_or_404(self.model, uuid=resource_uuid)

    def get(self, request, resource_uuid, format=None):
        instance = self.get_object(resource_uuid)
        serializer = self.serializer(instance)
        return Response(serializer.data)

class EmbedView(TemplateView):
    template_name = "pages/embed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "embed"
        return context

class ExtractView(TemplateView):
    template_name = "pages/extract.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "extract"
        return context