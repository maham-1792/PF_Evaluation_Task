# -*- coding: utf-8 -*-
"""Evaluation Numpy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FsP3N09emAO_ZvUKIAuvaHPN2L3JeVCo
"""

import keras
import random
import collections
import numpy as np
import matplotlib.pyplot as plt




def display_random_images_with_labels(d, n=10):
    """
        accept dataset in tuple form, first index
        is np arrays (images) and second is labels
        and display n random images with labels
        from it
        Inputs:
            d (tuple): dataset images, dataset labels on same indexs
            n (int): number of samples to display (default: 10)
        Output:
            None
    """
    choices = list(range(len(d[0])))
    for i in range(n):
        index = random.choice(choices)
        choices.remove(index)
        print("index:",index)
        print("Lable:",d[1][index])
        plt.imshow(d[0][index], cmap='gray')
        plt.show()

import keras.datasets.mnist as mnist
# Loading the dataset
dataset = mnist.load_data()
print(dataset)

(train_X, train_y), (test_X, test_y) = mnist.load_data()

#printing the shapes of the vectors
print('X_train: ' + str(train_X.shape))
print('Y_train: ' + str(train_y.shape))
print('X_test:  '  + str(test_X.shape))
print('Y_test:  '  + str(test_y.shape))

def display_random_images_with_labels(images, labels):
    num_images_to_display = 10
    random_indices = np.random.choice(len(images), num_images_to_display, replace=False)

    fig, axes = plt.subplots(1, num_images_to_display, figsize=(15, 3))
    for i, idx in enumerate(random_indices):
        image = images[idx]
        label = labels[idx]
        axes[i].imshow(image, cmap='gray')
        axes[i].set_title(f"Label: {label}")
        axes[i].axis('off')
    plt.show()

# Print the number of images in the training and testing datasets
print(f"There are {len(dataset[0][0])} images in the training dataset.")
print(f"There are {len(dataset[1][0])} images in the testing dataset.")
print("___________________")

# Print the shape of the first image in the training dataset
print(dataset[0][0][0].shape)
print("___________________")

# Print randomly selected 10 images with labels from the training dataset
print("Randomly printing 10 images with labels from the training dataset")
display_random_images_with_labels(dataset[0][0], dataset[0][1])
print("___________________")

# Print randomly selected 10 images with labels from the testing dataset
print("Randomly printing 10 images with labels from the testing dataset")
display_random_images_with_labels(dataset[1][0], dataset[1][1])
print("___________________")

# Print the number of labels in the training and testing datasets
print(f"There are {len(dataset[0][1])} labels in the training dataset for {len(dataset[0][0])} images in the training dataset.")
print(f"There are {len(dataset[1][1])} labels in the testing dataset for {len(dataset[1][0])} images in the testing dataset.")
print("___________________")

# Print the number of unique classes in the training dataset and the breakdown of each label
print(f"There are {len(set(dataset[0][1]))} unique classes in the training dataset.")
print("Breakdown of each label in the training dataset:")
print(dict(collections.Counter(dataset[0][1])))

# Print the number of unique classes in the testing dataset and the breakdown of each label
print(f"There are {len(set(dataset[1][1]))} unique classes in the testing dataset.")
print("Breakdown of each label in the testing dataset:")
print(dict(collections.Counter(dataset[1][1])))
print("__________")

def reduce_dataset(images, labels, num_per_label):
    reduced_images = []
    reduced_labels = []
    unique_labels = np.unique(labels)

    for label in unique_labels:
        indices = np.where(labels == label)[0]
        random_indices = np.random.choice(indices, num_per_label, replace=False)
        reduced_images.extend(images[random_indices])
        reduced_labels.extend(labels[random_indices])

    return np.array(reduced_images), np.array(reduced_labels)
    # Load the MNIST dataset from Keras
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reduce the size of the training and testing datasets
num_per_label_train = 600
num_per_label_test = 100
reduced_train_images, reduced_train_labels = reduce_dataset(train_images, train_labels, num_per_label_train)
reduced_test_images, reduced_test_labels = reduce_dataset(test_images, test_labels, num_per_label_test)

# Create a new dataset in the same format as the original dataset
new_dataset = ((reduced_train_images, reduced_train_labels), (reduced_test_images, reduced_test_labels))

# Print the size of the new reduced dataset
print(f"New training dataset size: {len(reduced_train_images)} images")
print(f"New testing dataset size: {len(reduced_test_images)} images")

num_images_to_display = 10
    random_indices = np.random.choice(len(images), num_images_to_display, replace=False)

    fig, axes = plt.subplots(1, num_images_to_display, figsize=(15, 3))
    for i, idx in enumerate(random_indices):
        image = images[idx]
        label = labels[idx]
        axes[i].imshow(image, cmap='gray')
        axes[i].set_title(f"Label: {label}")
        axes[i].axis('off')
    plt.show()


# Reduce the size of the training and testing datasets
num_per_label_train = 600
num_per_label_test = 100

def reduce_dataset(images, labels, num_per_label):


# Create a new dataset in the same format as the original dataset
    new_dataset = ((reduced_train_images, reduced_train_labels), (reduced_test_images, reduced_test_labels))

# Checking the shape of the first image in the new training dataset
print(new_dataset[0][0][0].shape)
print("___________________")

# Checking the size of the dataset
print(f"There are {len(new_dataset[0][1])} labels in the training dataset for {len(new_dataset[0][0])} images in the training dataset")
print(f"There are {len(new_dataset[1][1])} labels in the testing dataset for {len(new_dataset[1][0])} images in the testing dataset")
print("___________________")

# Checking the number of images per class
print(f"There are {len(set(new_dataset[0][1]))} unique classes in the training dataset")
print("Breakdown of each label in the training dataset:")
print(dict(collections.Counter(new_dataset[0][1])))

print(f"There are {len(set(new_dataset[1][1]))} unique classes in the testing dataset")
print("Breakdown of each label in the testing dataset:")
print(dict(collections.Counter(new_dataset[1][1])))
print("___________________")

# Checking the correctness of indexing of images and its labels
print("Randomly printing 10 images with labels from the training dataset")
display_random_images_with_labels(new_dataset[0][0], new_dataset[0][1])
print("___________________")
print("Randomly printing 10 images with labels from the testing dataset")
display_random_images_with_labels(new_dataset[1][0], new_dataset[1][1])
print("_____________")