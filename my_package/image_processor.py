from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_emboss_filter(self):
        return self.image.filter(ImageFilter.EMBOSS)

    def add_watermark(self, text="Вариант 5"):
        watermark_image = self.image.copy()
        draw = ImageDraw.Draw(watermark_image)
        width, height = self.image.size
        font = ImageFont.truetype("arial.ttf", 36)
        # Используем textbbox для получения размеров текста
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        position = (width - text_width - 10, height - text_height - 10)
        draw.text(position, text, font=font, fill=(255, 255, 255, 128))
        return watermark_image
