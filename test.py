"""
1.01 概述与环境搭建  test.py
"""

import cv2 as cv

src = cv.imread("F:/Pictures/2.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi, Python!")
