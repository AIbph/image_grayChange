#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
from PIL import Image
from pylab import *
from numpy import *


if __name__ == '__main__':
    im = array(Image.open("./img/test.jpg").convert("L"))
    figure()
    contour(im, origin='image')

    # 对图像进行反相处理
    im2 = 255 - im
    figure()
    contour(im2, origin='image')

    # 将图像像素值变换到 100...200 区间
    im3 = (100.0/255) * im + 100
    figure()
    contour(im3, origin='image')

    # 对图像像素值求平方后得到的图像
    im4 = 255.0 * (im/255.0)**2
    figure()
    contour(im4, origin='image')

    show()