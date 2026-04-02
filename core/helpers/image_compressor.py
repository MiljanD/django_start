from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


class ImageCompressor:
    def __init__(self, max_size=(1920, 1080), quality=80, output_format = "WEBP"):
        self.max_size = max_size
        self.quality = quality
        self.output_format = output_format

    def compress(self, image_field):
        img = Image.open(image_field)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")


        if img.width > self.max_size[0] or img.height > self.max_size[1]:
            img.thumbnail(self.max_size, Image.LANCZOS)

        buffer = BytesIO()
        img.save(buffer, format=self.output_format, quality=self.quality)
        buffer.seek(0)

        return ContentFile(buffer.read())

