# Scenario 7: Image Augmentation
# Task: Create an image augmentation pipeline using TensorFlow/Keras
# with rotation, horizontal flip, and zoom transformations.

from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_augmentation():
    datagen = ImageDataGenerator(
        rotation_range=20,
        horizontal_flip=True,
        zoom_range=0.2
    )
    return datagen


if __name__ == "__main__":
    print("Image Augmentation Pipeline Created")