"""
2.02 图像加载与保存  tutorial_1.py
"""
import cv2 as cv
import numpy as np  # 科学计数包


def video_demo():
    """调用摄像头"""
    capture = cv.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    """获取图片信息"""
    print(type(image))  # 文件类别
    print(image.shape)  # 高，宽，通道数
    print(image.size)  # 像素大小=高*宽*通道数
    print(image.dtype)  # 字节类型
    pixel_data = np.array(image)
    print(pixel_data)


print("---------- Hello Python ----------")
src = cv.imread("F:/Pictures/2.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 把图片用灰度表示
cv.imwrite("F:/DIP/result.png", gray)
video_demo()
cv.waitKey(0)

cv.destroyAllWindows()
