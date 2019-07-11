
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
 
classes = ["yezhi","kangshifu","yogurt"]#红绿灯检测
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
def convert_annotation(image_id):
    
    in_file = open('D:\file\yolo v3\data\img%s.xml'%(image_id))
    
    out_file = open('D:\file\yolo v3\data\img%s.txt'%(image_id),'w')#生成txt格式文件
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')  
    w = int(size.find('width').text)
    h = int(size.find('height').text)
 
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes :
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')   
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
image_ids_train = open("./data").read().strip().split()#list格式只有000000 000001
 
#image_ids_val = open('/home/*****/darknet/scripts/VOCdevkit/voc/list').read().strip().split()
 
 
 
list_file_train = open('boat_train.txt', 'w')     
list_file_val = open('boat_val.txt', 'w')     
 
 
for image_id in image_ids_train:
    list_file_train.write('D:\file\yolo v3\data\JPEGImages\%s.jpg\n'%(image_id))  
    convert_annotation(image_id)   
list_file_train.close()      #只生成训练集，自己根据自己情况决定
 
 
 
 
#for image_id in image_ids_val:
 
#    list_file_val.write('/home/*****/darknet/boat_detect/images/%s.jpg\n'%(image_id))  
#    convert_annotation(image_id)
#list_file_val.close()