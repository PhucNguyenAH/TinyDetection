import json
import os

train_anno = json.load(open('data/coco/annotations/instances_train2017.json'))
print(train_anno.keys())
print(train_anno['images'][0])
print(train_anno['annotations'][0])
print(train_anno['categories'])
print("info",train_anno['info'])
print("licenses",train_anno['licenses'])

print("number of images in anno", len(train_anno['images']))

src = "data/coco/train2017/"

src_files = os.listdir(src)
print("Number of images in data:",len(src_files))

for cat in train_anno['categories']: 
    if cat['supercategory']=='person':
        print(cat)
