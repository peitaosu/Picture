import os
from PIL import Image, ImageDraw, ImageFont


def add_watermark(image, watermark, pos_x, pos_y, save="new.jpg", font="C:\\Windows\\Fonts\\Arial.ttf", size=50, color="#FFFFFF"):
    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    if pos_x < 0:
        pos_x = width + pos_x
    if pos_y < 0:
        pos_y = height + pos_y
    draw.text((pos_x, pos_y), watermark, font=ImageFont.truetype(font, size), fill=color)
    img.save(save, 'jpeg')
    return 0

if __name__ == '__main__':
    in_folder = "."
    for image in os.listdir(in_folder):
        image_name = ".".join(image.split(".")[:-1])
        add_watermark(os.path.join(in_folder, image), "Tony Su", -700, -300, os.path.join(in_folder, image_name + "_new.jpg"), "C:\\Windows\\Fonts\\Halimun.ttf", 100, color="#FFFFFF")
