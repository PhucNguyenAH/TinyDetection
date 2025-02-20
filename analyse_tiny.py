import json
import os
import cv2
import matplotlib.pyplot as plt


train_root = 'data/tinyperson/train/'
test_root = 'data/tinyperson/test/'

train_anno = json.load(open('data/tinyperson/annotations/tiny_set_train.json'))
test_anno = json.load(open('data/tinyperson/annotations/tiny_set_test.json'))

print(train_anno.keys())
i=0
while train_anno['annotations'][i]["uncertain"]==False:
    i+=1
print(train_anno['images'][i])
print(train_anno['annotations'][i])
print(train_anno['categories'])
print("number of images in anno", len(train_anno['images']))

# src0 = "data/tinyperson/train/labeled_dense_images/"
src1 = "data/tinyperson/train/labeled_images/"
# src2 = "data/tinyperson/train/no_label_images/"
src3 = "data/tinyperson/train/pure_bg_images/"

# src_files = os.listdir(src0) + os.listdir(src1) + os.listdir(src2) + os.listdir(src3)
src_files =  os.listdir(src1) + os.listdir(src3)
print("Number of images in data:",len(src_files))

dir_type = set()
for img_path in train_anno['images']:
    name = img_path['file_name'].split("/")[0]
    dir_type.add(name)
print("dir_type",dir_type)

for img_path in train_anno['images']:
    if not os.path.exists(train_root+img_path['file_name']):
        print("hello")

for img_path in test_anno['images']:
    if not os.path.exists(test_root+img_path['file_name']):
        print("hi")
img = cv2.imread(train_root+train_anno['images'][0]['file_name'])

cv2.imwrite("img_test.jpg",img)