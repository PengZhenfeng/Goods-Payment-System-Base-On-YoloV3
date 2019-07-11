import cv2
import os
import numpy as np
import qrcode
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import PIL.Image
from usage_function import *





#获取商品图片
cap = cv2.VideoCapture(0)
while (1):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite("./../workdir/object.jpg", frame)
        training()
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()









object_list = data_opera()
if object_list != [ '']:
    goods_list = get_goods(object_list)
    price_list = get_price(object_list)
    print(goods_list)
    print(price_list)
    string_data = output(goods_list,price_list)
    create_qrcode(string_data)
    opecv_muti_pic()
else:
    print("no good has been detection\n")