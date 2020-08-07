import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import argparse
import sys

# position maps
INFO = {"High": {"Rec": [(24, 452), (225, 625), (750, 480), "./base_images/HighDenRec.png"],
                 "Square": [(24, 330), (180, 525), (730, 540), "./base_images/HighDenSquare.png"]
                },
        "Med": {"Rec": [(28, 456), (225, 630), (755, 475), "./base_images/MedDenRec.png"],
                   "Square": [(24, 330), (180, 530), (730, 540), "./base_images/MedDenSquare.png"]
                  }
        }


def putText(image, outimage, h_text, h_pos, w_text, w_pos, l_text, l_pos):
    # Convert the image to RGB (OpenCV uses BGR)
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Pass the image to PIL
    pil_im = Image.fromarray(cv2_im_rgb)

    draw = ImageDraw.Draw(pil_im)

    # get font
    font = ImageFont.truetype("./fonts/arial-rounded-mt-bold-grassetto.ttf", 48)

    # Draw the text
    draw.text(h_pos, h_text + "”", font=font, fill=(0, 0, 0))
    draw.text(w_pos, w_text + "”", font=font, fill=(0, 0, 0))
    draw.text(l_pos, l_text + "”", font=font, fill=(0, 0, 0))

    # Get back the image to OpenCV
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    cv2.imwrite(outimage, cv2_im_processed)


def create_arg_parser():
    """ Create and returns the ArgumentParser object."""

    parser = argparse.ArgumentParser(prog="Dimension Writer",
                                     description="takes in h w l and creates text over base images")

    parser.add_argument("-c",
                        help="cut of foam. ex: Rec, Square")
    parser.add_argument("-q",
                        help="quality of foarm. ex: High, Med")
    parser.add_argument("-t",
                        help="height dimension")
    parser.add_argument("-w",
                        help="width dimension")
    parser.add_argument("-l",
                        help="length dimension")
    parser.add_argument("-o",
                        help="path for output image. png format")

    return parser


if __name__ == '__main__':
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])

    print(parsed_args)

    outimage = parsed_args.o
    Cut = parsed_args.c
    Qual = parsed_args.q
    h_text = parsed_args.t
    w_text = parsed_args.w
    l_text = parsed_args.l
    image = cv2.imread(INFO[Qual][Cut][3], cv2.IMREAD_UNCHANGED)

    putText(image, outimage, h_text, INFO[Qual][Cut][0], w_text, INFO[Qual][Cut][1], l_text, INFO[Qual][Cut][2])