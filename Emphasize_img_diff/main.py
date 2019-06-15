import sys
import numpy as np
import cv2


def main():

    img_src1 = cv2.imread("img_test/01.jpg", 1)
    img_src2 = cv2.imread("img_test/01.jpg", 1)

    fgbg = cv2.bgsegm.createBackgroundSubstractorMOG()

    fgmask = fgbg.apply(img_src1)
    fgmask = fgbg.apply(img_src2)


if __name__ == "__main__":
    main()
