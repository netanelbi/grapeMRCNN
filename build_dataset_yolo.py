import os
import numpy as np
import random
import shutil

def create_dataset(dataset_folder,dataset_type,data_folder,image_list):

	for image in image_list:

		image_src_path=data_folder+image+'.jpg'
		image_dst_path=dataset_folder+os.sep+'images'+os.sep+dataset_type+os.sep+image+'.jpg'
		shutil.copy2(image_src_path,image_dst_path)

		bbox_src_path = data_folder + image + '.txt'
		bbox_dst_path = dataset_folder+os.sep+'labels'+os.sep+dataset_type+os.sep+image+'.txt'
		shutil.copy2(bbox_src_path, bbox_dst_path)

		# mask_src_path = data_folder + image + '.npz'
		# mask_dst_path = dataset_folder + os.sep + image + '.npz'
		# shutil.copy2(mask_src_path, mask_dst_path)


data_folder='./wgisd/data/'
test_files ='./wgisd/test.txt'
train_files ='./wgisd/train.txt'

ROOT_DIR = os.path.abspath("./grapeMRCNN/")
print(ROOT_DIR)

# load the names of the images
with open(train_files, 'r') as fp:
    data_list = fp.readlines()
# load the names of the images for test
with open(test_files, 'r') as fp:
    data_list_test = fp.readlines()

data_list = set([i[:-1] for i in data_list])
data_list_test = set([i[:-1] for i in data_list_test])
# split
data_list=sorted(data_list)
random.shuffle(data_list)

i = int(len(data_list) * 0.8)
data_list_train = data_list[:i]
data_list_val = data_list[i:]

#create dataset folder
dataset_folder= os.path.sep.join([ROOT_DIR,"dataset"])
if not os.path.exists(os.path.sep.join([dataset_folder,'images'])):
	os.makedirs(os.path.sep.join([dataset_folder,'images']))
if not os.path.exists(os.path.sep.join([dataset_folder,'labels'])):
	os.makedirs(os.path.sep.join([dataset_folder,'labels']))
if not os.path.exists(dataset_folder):
	os.makedirs(dataset_folder)

#build train dataset

if not os.path.exists(os.path.sep.join([dataset_folder,'images','train'])):
	os.makedirs(os.path.sep.join([dataset_folder,'images','train']))
if not os.path.exists(os.path.sep.join([dataset_folder,'labels','train'])):
	os.makedirs(os.path.sep.join([dataset_folder,'labels','train']))
create_dataset(dataset_folder,'train',data_folder,data_list_train)

# build Validation dataset
if not os.path.exists(os.path.sep.join([dataset_folder,'images','val'])):
	os.makedirs(os.path.sep.join([dataset_folder,'images','val']))
if not os.path.exists(os.path.sep.join([dataset_folder,'labels','val'])):
	os.makedirs(os.path.sep.join([dataset_folder,'labels','val']))
create_dataset(dataset_folder,'val',data_folder,data_list_val)

# build test dataset
if not os.path.exists(os.path.sep.join([dataset_folder,'images','test'])):
	os.makedirs(os.path.sep.join([dataset_folder,'images','test']))
if not os.path.exists(os.path.sep.join([dataset_folder,'labels','test'])):
	os.makedirs(os.path.sep.join([dataset_folder,'labels','test']))
create_dataset(dataset_folder,'test',data_folder,data_list_test)

#for i in data_list:
#   print(i)

print("\ntrain:{},val:{},test:{}".format(len(data_list_train),len(data_list_val),len(data_list_test)))


