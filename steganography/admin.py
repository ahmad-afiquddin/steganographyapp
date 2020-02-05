from django.contrib import admin
from steganography.models import EmbedImage, ExtractImage

# Register your models here.
@admin.register(EmbedImage)
class EmbedImageAdmin(admin.ModelAdmin):

    list_display = ('uuid',)

@admin.register(ExtractImage)
class ExtractImageAdmin(admin.ModelAdmin):

    list_display = ('uuid',)