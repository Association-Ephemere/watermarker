from PIL import Image, ImageFile
import math
import os
import sys
from path import Path



def load_image(path : str) -> ImageFile:
    return Image.open(path)

def get_watermark():
    wm_path = os.path.join(Path((__file__)).parent, "assets/watermark/watermark.png")

    return Image.open(wm_path)

def apply_watermark(img: Image.Image, wm : Image.Image, x_ratio: float, margin: tuple[float, float]) -> Image.Image:
    if wm is None:
        wm = get_watermark()

    img_ref = math.sqrt(img.width * img.height)
    wm_ref = math.sqrt(wm.width * wm.height)
    scale = (img_ref * x_ratio) / wm_ref

    wm_width = math.ceil(wm.width * scale)
    wm_height = math.ceil(wm.height * scale)
    wm_resized = wm.resize((wm_width, wm_height), Image.Resampling.BICUBIC)

    margin_x = round(img_ref * margin[0])
    margin_y = round(img_ref * margin[1])

    pos_x = img.width - wm_width - margin_x
    pos_y = img.height - wm_height - margin_y

    result = img.copy()
    result.paste(wm_resized, (pos_x, pos_y), wm_resized)

    return result