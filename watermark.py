#!/usr/bin/env python3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import glob

def watermark_text(input_image_path,output_image_path,text, pos):
    photo = Image.open(input_image_path)
    width, height = photo.size
    # make the image editable
    drawing = ImageDraw.Draw(photo)

    font = ImageFont.truetype("Roboto-Black.ttf", 20)

    text_width, text_height = drawing.textsize(text, font)
    pos = width - text_width, (height - text_height) - 50
    drawing.text(pos, text, fill="#ffffff", font=font)
    photo.save(output_image_path)


if __name__ == '__main__':
    jpg_list = glob.glob('*.jpg')
    for jpg in jpg_list:
        name,_ = jpg.split('.')
        watermark_text(jpg, 'watermarked_'+name+'.jpg',text='© Pinehead Gurus Ltd',pos=(0, 0))
