from PIL import Image, ImageChops, ImageEnhance
import os

def ela(origin, quality=90, save_path=None):

    ori_im = Image.open(origin)
    tmp = origin + ".tmp"
    ori_im.save(tmp, 'JPEG', quality=quality)

    tmp_im = Image.open(tmp)
    ela_im = ImageChops.difference(ori_im, tmp_im)

    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    scale = 255.0/max_diff
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
    if save_path is not None:
        ela_im.save(save_path)
    else:
        ela_im.show()
    os.remove(tmp)

if __name__=="__main__":
    ela("Input.JPG")