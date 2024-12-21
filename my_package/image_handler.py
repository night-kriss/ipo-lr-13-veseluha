from PIL import Image
from datetime import datetime

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path)
        return self.image

    def save_image(self, image, suffix=""):
        current_date = datetime.now().strftime("%Y%m%d")
        new_filename = f"{self.image_path.split('.')[0]}_{current_date}{suffix}.{self.image_path.split('.')[-1]}"
        image.save(new_filename)
        print(f"Image saved as {new_filename}")

    def resize_image(self, scale=0.5):
        if self.image:
            new_size = (int(self.image.width * scale), int(self.image.height * scale))
            resized_image = self.image.resize(new_size)
            return resized_image
        else:
            raise ValueError("Image not loaded")
