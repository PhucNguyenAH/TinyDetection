import json

train_anno = json.load(open('data/tinyperson/annotations/tiny_set_train.json'))
test_anno = json.load(open('data/tinyperson/annotations/tiny_set_test.json'))

for img_path in train_anno['images']:
    new_path = img_path['file_name'].split("/")[-1]
    img_path['file_name'] = new_path

for img_path in test_anno['images']:
    new_path = img_path['file_name'].split("/")[-1]
    img_path['file_name'] = new_path

train_anno['info'] = dict()
test_anno['info'] = dict()
train_anno['licenses'] = []
test_anno['licenses'] = []
with open('data/tinyperson/annotations/tiny_set_train_new.json', 'w') as f:
    json.dump(train_anno, f)

with open('data/tinyperson/annotations/tiny_set_test_new.json', 'w') as f:
    json.dump(test_anno, f)