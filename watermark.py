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
    import os, optparse
    parser = optparse.OptionParser()
    parser.add_option("--in_folder", dest="in_folder", help="read pictures from folder")
    parser.add_option("--watermark", dest="watermark", help="watermark text")
    parser.add_option("--pos_x", dest="pos_x", help="watermark position: x")
    parser.add_option("--pos_y", dest="pos_y", help="watermark position: y")
    parser.add_option("--font", dest="font", help="watermark font")
    parser.add_option("--size", dest="size", help="watermark size")
    parser.add_option("--color", dest="color", help="watermark color")
    (options, args) = parser.parse_args()

    for image in os.listdir(options.in_folder):
        image_name = ".".join(image.split(".")[:-1])
        add_watermark(os.path.join(options.in_folder, image), options.watermark, options.pos_x, options.pos_y, os.path.join(options.in_folder, image_name + "_marked.jpg"), options.font, options.size, options.color)
