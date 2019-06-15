import sys
import numpy as np
import cv2


def main():

    img_src1 = cv2.imread("img_test/01.jpg", 1)
    img_src2 = cv2.imread("img_test/02.jpg", 1)

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

    fgmask = fgbg.apply(img_src1)
    fgmask = fgbg.apply(img_src2)

    cv2.imshow('frame', fgmask)

    bg_diff_path = './diff.jpg'
    cv2.imwrite(bg_diff_path, fgmask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
