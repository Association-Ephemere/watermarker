from PIL import Image, ImageFile
import os
import sys

import watermarker


def treat_image(p):
    img = watermarker.load_image(p)

    img_wm = watermarker.apply_watermark(img, wm, 0.09, (0.02, 0.02))

    img_wm.save(os.path.join("data/output/", f))


if __name__ == "__main__":
    # args = sys.argv

    # if len(args) <= 1:
    #     raise Exception("Missing path to image")



    wm = watermarker.get_watermark()

    if not os.path.exists("data/output"):
        os.mkdir("data/output")

    files = os.listdir("data/input")

    for i in range(len(files)):
        f = files[i]

        if f == ".gitkeep":
            continue

        print(f"Starting {f}...", end=" ",flush=True)

        p = os.path.join("data/input/", f)

        if not os.path.exists(p):
            raise Exception(f"\"{p}\" does not exist")

        treat_image(p)

        print(f"Done. {round(100 * i / len(files), 2)}%",flush=True)

        
    
    