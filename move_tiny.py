import os
import shutil
src0 = "data/tinyperson/train/labeled_images/"
src1 = "data/tinyperson/train/pure_bg_images/"

dest = "data/tinyperson/train_all/"
if not os.path.exists(dest):
    os.makedirs(dest)
src_files = os.listdir(src0)
for file_name in src_files:
    full_file_name = os.path.join(src0, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)
src_files = os.listdir(src1)
for file_name in src_files:
    full_file_name = os.path.join(src1, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)


src0 = "data/tinyperson/test/labeled_images/"
src1 = "data/tinyperson/test/pure_bg_images/"

dest = "data/tinyperson/test_all/"
if not os.path.exists(dest):
    os.makedirs(dest)
src_files = os.listdir(src0)
for file_name in src_files:
    full_file_name = os.path.join(src0, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)
src_files = os.listdir(src1)
for file_name in src_files:
    full_file_name = os.path.join(src1, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)

