from my_package import ImageHandler, ImageProcessor

# Инициализация и загрузка изображения
image_path = "image_1.jpg"
handler = ImageHandler(image_path)
original_image = handler.load_image()

# Масштабирование изображения до 50%
resized_image = handler.resize_image()

# Сохранение масштабированного изображения с текущей датой
handler.save_image(resized_image, suffix="_resized")

# Инициализация процессора изображения
processor = ImageProcessor(resized_image)

# Применение фильтра "Эмбосс"
embossed_image = processor.apply_emboss_filter()

# Сохранение изображения с фильтром
handler.save_image(embossed_image, suffix="_embossed")

# Добавление водяного знака
watermarked_image = processor.add_watermark()

# Сохранение изображения с водяным знаком
handler.save_image(watermarked_image, suffix="_watermarked")

