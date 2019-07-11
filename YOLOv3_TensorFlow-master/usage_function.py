import cv2
import os
import numpy as np
import qrcode
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import PIL.Image

def training():
    '''执行训练命令'''
    #   os.system("cd YOLOv3_TensorFlow-master")
    os.system(
        "python test_single_image.py ../workdir/object.jpg --anchor_path ./data/yolo_anchors.txt --restore_path ./checkpoint/model-step_600_loss_6.172093_lr_0.001 --class_name_path ./data/my_data/my_classes.names")
    #	os.system("cd ../../yolo v3")

    print("finish detection")

def opecv_muti_pic():
    '''整合付款码和效果图，并显示'''
    # 图1
    img = cv2.imread('./../workdir/object_result.jpg')
    # 图2
    img2 = cv2.imread('./../workdir/pay.jpg')
    # 图集
    im1 = cv2.resize(img, (600, 600))
    im2 = cv2.resize(img2, (600, 600))
    imgs = np.hstack([im1,im2])
    # 展示多个
    cv2.imshow("pay windows", imgs)
    #等待关闭
    cv2.waitKey(0)

def data_opera():
        '''返回识别到的商品标签'''
        with open('./../workdir/object.json') as c_obj:
            classes = c_obj.read()
        #    print(classes)
        classes = classes.replace('"[', '')
        classes = classes.replace(']"', '')

        #   print(classes)
        classes_list = classes.split(" ")
        #    classes_list = classes_list[1:-1]
        #   print(classes_list)

        return classes_list

def get_goods(object_list):
        '''根据标签转换商品名'''
        goods_list = []
        with open('./data/my_data/my_classes.names') as goods_obj:
            content = goods_obj.read().splitlines()
        i = 0
        while i < len(object_list):
            goods_list.append(content[int(object_list[i])])
            i += 1

        return goods_list

def get_price(object_list):
        '''根据标签获取商品价格'''
        price_list = []
        with open('./../workdir/price.txt') as price_obj:
            content = price_obj.read().splitlines()
        i = 0
        while i < len(object_list):
            price_list.append(content[int(object_list[i])])
            i += 1

        return price_list

def output(goods_list, price_list):
        '''计算商品总价'''
        i = 0
        data = 'the goods you buy are following:\n'
        while i < len(goods_list):
            data = data + goods_list[i] + '\t' + price_list[i] + '\n'
            i += 1
        sum = 0
        for per_price in price_list:
            sum += float(per_price)
        #    sum = float('%.2f'%sum)
        data = data + "you should pay " + str(sum) + '\n'
        print(data)
        return data

def create_qrcode(data):
        '''生成二维码'''
        img = qrcode.make(data)
        img.save('./../workdir/pay.jpg')