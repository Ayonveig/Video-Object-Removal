import argparse
from masking.masking import mask
from inpainting.inpainting import inpaint
from inpainting2.inpainting2 import inpaint2

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", required = True, help = "path to images or videos")
ap.add_argument("--flow", action = "store_true")
args = ap.parse_args()

mask(args)
if args.flow:
    inpaint(args)
else:
    inpaint2(args)
