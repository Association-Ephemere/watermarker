from src.watermarker import load_image, get_watermark
from PIL import Image, ImageFile
import pytest

def test_load_image():
    img : ImageFile = load_image("tests/assets/wei_no_wm.jpg")

    assert img is not None



def test_get_watermark():
    assert get_watermark() is not None