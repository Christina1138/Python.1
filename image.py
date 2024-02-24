from PIL import Image
from PIL import ImageFilter

with Image.open("photo.jpeg") as original:
    print("Розмір зображення: ", original.size )
    print("Формат зображення: ", original.format)
    print("Колірний тип: ", original.mode)

    b_w = original.convert("L")
    b_w.save ("b_w.jpeg")

    blurimg = original.filter(ImageFilter.BLUR)
    blurimg.save ("blur.jpeg")

    rotateimg = original.transpose(Image.ROTATE_90)
    rotateimg.save("rotate.jpeg")

    rotateimg = original.transpose(Image.ROTATE_180)
    rotateimg.save("rotate.jpeg")

    rotateimg = original.transpose(Image.ROTATE_270)
    rotateimg.save("rotate.jpeg")

    mirriwimg = original.transpose(Image.FLIP_LEFT_RIGHT)
    mirriwimg.save("mirror.jpeg")

    box = (250, 100, 600, 400)
    crop = original.crop(box)
    crop.save("crop.jpeg")