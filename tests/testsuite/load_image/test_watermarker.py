from src.watermarker import load_image, get_watermark, apply_watermark
from PIL import Image, ImageFile, ExifTags
import pytest

def test_load_image():
    img : ImageFile = load_image("tests/assets/wei_no_wm.jpg")

    assert img is not None



def test_get_watermark():
    assert get_watermark() is not None


def test_exif_orientation_rotation(tmp_path):
    # Create a horizontal image (200x100) with EXIF Orientation 6 (90 deg CW -> should become 100x200 vertical)
    img = Image.new("RGB", (200, 100), color=(255, 0, 0))
    exif = img.getexif()
    exif[ExifTags.Base.Orientation] = 6

    img_path = tmp_path / "rotated.jpg"
    img.save(img_path, exif=exif.tobytes())

    loaded = load_image(str(img_path))
    assert loaded.size == (100, 200)
    assert loaded.getexif().get(ExifTags.Base.Orientation) is None

    # Also test apply_watermark directly on an un-transposed image with EXIF orientation
    raw_img = Image.open(str(img_path))
    wm = Image.new("RGBA", (20, 20), color=(0, 255, 0, 255))
    watermarked = apply_watermark(raw_img, wm, 0.2, (0.05, 0.05))
    assert watermarked.size == (100, 200)
    # Check that watermark was pasted at the bottom-right of the vertical image
    assert watermarked.getpixel((90, 185)) == (0, 255, 0)
