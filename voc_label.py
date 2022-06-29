import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob

#sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = [ 'sedge', 'filed bindweed', 'cirsium','chenopodium','cotton','bluegrass'  ]


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

def convert_annotation(image_name):
    in_file = open('./datasets/VOC2012/Annotations/'+image_name[:-3]+'xml')
    out_file = open('E://pythonwork//program//yolov5//datasets//VOC2012//labels//'+image_name[:-3]+'txt', 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        #difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes :
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

if __name__=='__main__':
    for image_path in glob.glob("E://pythonwork//program//yolov5//datasets//VOC2012//JPEGImages//*.jpg"):
        image_name=image_path.split('\\')[-1]
        convert_annotation(image_name)
# def convert_annotation(year, image_id):
#     in_file = open('E://pythonwork//program//yolov5//datasets//VOC2012//Annotations//%s.xml'%(year, image_id))
#     out_file = open('E://pythonwork//program//yolov5//datasets//VOC2012//labels//%s.txt'%(year, image_id), 'w')
#     tree=ET.parse(in_file)
#     root = tree.getroot()
#     size = root.find('size')
#     w = int(size.find('width').text)
#     h = int(size.find('height').text)
#
#     for obj in root.iter('object'):
#         difficult = obj.find('difficult').text
#         cls = obj.find('name').text
#         if cls not in classes or int(difficult) == 1:
#             continue
#         cls_id = classes.index(cls)
#         xmlbox = obj.find('bndbox')
#         b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
#         bb = convert((w,h), b)
#         out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
#
# wd = getcwd()

# for year, image_set in sets:
#     if not os.path.exists('E://pythonwork//program//yolov5//datasets//VOC2012//labels/'%(year)):
#         os.makedirs('E://pythonwork//program//yolov5//datasets//VOC2012//labels/'%(year))
#     image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt'%(year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n'%(wd, year, image_id))
#         convert_annotation(year, image_id)
#     list_file.close()


