# External dependencies
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid
import sys

# Local functions
import uuid
from steganography.steganography_image import Payload, Carrier

# Create your models here.
class EmbedImage(models.Model):

    uuid = models.UUIDField(
        'UUID',
        max_length=40,blank=True, default=uuid.uuid4, unique=True,
        help_text="Unique uuid", editable=False
    )
    image = models.ImageField(
        default=None, blank=True, null=True,
        upload_to="photos",
        help_text="Carrier",
    )
    text = models.TextField(
        default=None, blank=True, null=True,
        help_text="Payload"
    )
    payload = models.TextField(
        default=None, blank=True, null=True,
        help_text="Compressed payload"
    )

    def save(self, *args, **kwargs):
        payload = Payload(self.text)
        payload.create_json()
        json_payload = payload.json
        carrier = Carrier(self.image)
        carrier.embed_payload(payload)
        image = Image.fromarray(carrier.img.astype('uint8'), 'RGBA')
        output = BytesIO()
        image.save(output, format="PNG", quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" %self.image.name.split('.')[0], 'image/png', sys.getsizeof(output), None)

        self.payload = json_payload
        super(EmbedImage, self).save(*args, **kwargs)

class ExtractImage(models.Model):

    uuid = models.UUIDField(
        'UUID',
        max_length=40,blank=True, default=uuid.uuid4, unique=True,
        help_text="Unique uuid", editable=False
    )
    image = models.ImageField(
        default=None, blank=True, null=True,
        upload_to="photos",
        help_text="Carrier",
    )
    text = models.TextField(
        default=None, blank=True, null=True,
        help_text="Payload"
    )
    payload = models.TextField(
        default=None, blank=True, null=True,
        help_text="Compressed payload"
    )

    def clean(self, *args, **kwargs):
        carrier = Carrier(self.image)
        if not carrier.payloadExists():
            raise ValidationError("No text detected")
        super(ExtractImage, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        carrier = Carrier(self.image)
        payload = carrier.extract_payload()
        payload = Payload(None, payload)
        
        self.payload = payload.json
        self.text = payload.rawData
        super(ExtractImage, self).save(*args, **kwargs)


