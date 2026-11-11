from PIL import Image, ImageFile, ImageOps
import math
import os
import sys
from path import Path



def load_image(path : str) -> Image.Image:
    return ImageOps.exif_transpose(Image.open(path))

def get_watermark():
    wm_path = os.path.join(Path((__file__)).parent, "assets/watermark/watermark.png")

    return Image.open(wm_path)

def apply_watermark(img: Image.Image, wm : Image.Image, x_ratio: float, margin: tuple[float, float]) -> Image.Image:
    if wm is None:
        wm = get_watermark()

    result = ImageOps.exif_transpose(img)

    img_ref = math.sqrt(result.width * result.height)
    wm_ref = math.sqrt(wm.width * wm.height)
    scale = (img_ref * x_ratio) / wm_ref

    wm_width = math.ceil(wm.width * scale)
    wm_height = math.ceil(wm.height * scale)
    wm_resized = wm.resize((wm_width, wm_height), Image.Resampling.BICUBIC)

    margin_x = round(img_ref * margin[0])
    margin_y = round(img_ref * margin[1])

    pos_x = result.width - wm_width - margin_x
    pos_y = result.height - wm_height - margin_y

    result.paste(wm_resized, (pos_x, pos_y), wm_resized)

    return result