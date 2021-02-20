import os, shutil
from pathlib import Path

original_dataset_dir = os.path.abspath('/Users/jacob/OneDrive/Desktop/GitHub/Deep-Learning-With-Python-Exercises/dogs-vs-cats/train')

base_dir = os.path.abspath('/Users/jacob/OneDrive/Desktop/GitHub/Deep-Learning-With-Python-Exercises/cats_and_dogs_small')

os.chdir(base_dir)

# os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')

# os.mkdir(train_dir)

validation_dir = os.path.join(base_dir, 'validation')

# os.mkdir(validation_dir)

test_dir = os.path.join(base_dir, 'test')

# os.mkdir(test_dir)


train_cats_dir = os.path.join(train_dir, 'cats')

# os.mkdir(train_cats_dir)

train_dogs_dir = os.path.join(train_dir, 'dogs')

# os.mkdir(train_dogs_dir)


validation_cats_dir = os.path.join(validation_dir, 'cats')

# os.mkdir(validation_cats_dir)

validation_dogs_dir = os.path.join(validation_dir, 'dogs')

# os.mkdir(validation_dogs_dir)


test_cats_dir = os.path.join(test_dir, 'cats')

# os.mkdir(test_cats_dir)

test_dogs_dir = os.path.join(test_dir, 'dogs')

# os.mkdir(test_dogs_dir)


#training cats images
fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
	src = os.path.join(original_dataset_dir, fname)
	dst = os.path.join(train_cats_dir, fname)
	shutil.copyfile(src, dst)

#validation cats images
fnames = ['cat.{}.jpg'.format(i) for i in range(1000,1500)]
for fname in fnames:
	src = os.path.join(original_dataset_dir, fname)
	dst = os.path.join(validation_cats_dir, fname)
	shutil.copyfile(src,dst)

#test cat images
fnames = ['cat.{}.jpg'.format(i) for i in range(1500,2000)]
for fname in fnames:
	src = os.path.join(original_dataset_dir, fname)
	dst = os.path.join(test_cats_dir, fname)
	shutil.copyfile(src, dst)

#dogs training images
fnames = ['dog.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
	src = os.path.join(original_dataset_dir, fname)
	dst = os.path.join(train_dogs_dir, fname)
	shutil.copyfile(src, dst)

#dogs validation images
fnames = ['dog.{}.jpg'.format(i) for i in range(1000,1500)]
for fname in fnames:
	src = os.path.join(original_dataset_dir, fname)
	dst = os.path.join(validation_dogs_dir, fname)
	shutil.copyfile(src, dst)

#dogs test images
fnames = ['dog.{}.jpg'.format(i) for i in range(1500,2000)]
for fname in fnames:
	src = os.path.join(original_dataset_dir, fname)
	dst = os.path.join(test_dogs_dir, fname)
	shutil.copyfile(src, dst)

