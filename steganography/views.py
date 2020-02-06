# External dependencies
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Local dependencies, import serializers
from steganography.serializers import EmbedImageSerializer, ExtractImageSerializer
# import models
from steganography.models import EmbedImage, ExtractImage


class EmbedImageCreateView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = EmbedImage.objects.all()

    def post(self, request, format=None):
        serializer = EmbedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExtractImageCreateView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = ExtractImage.objects.all()

    def post(self, request, format=None):
        serializer = ExtractImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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