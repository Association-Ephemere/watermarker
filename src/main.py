from PIL import Image, ImageFile
import os
import sys

import watermarker

if __name__ == "__main__":
    # args = sys.argv

    # if len(args) <= 1:
    #     raise Exception("Missing path to image")



    wm = watermarker.get_watermark()

    if not os.path.exists("data/output"):
        os.mkdir("data/output")

    for f in os.listdir("data/input"):
        if f == ".gitkeep":
            continue

        p = os.path.join("data/input/", f)

        if not os.path.exists(p):
            raise Exception(f"\"{p}\" does not exist")

        img = watermarker.load_image(p)

        img_wm = watermarker.apply_watermark(img, wm, 0.09, (0.02, 0.02))

        img_wm.save(os.path.join("data/output/", f))

        
    
    