####################################################
################ Incomplete ########################
####################################################
####################################################


import numpy as np
import tensorflow as tf
import cv2
from sklearn.model_selection import train_test_split

# Loading the Dataset
image_paths = ['image1.png', 'image2.png', 'image3.png']  # List of image file paths
labels = [0, 1, 2]  # List of corresponding labels

# Load and preprocess images
images = []
for path in image_paths:
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    image = cv2.resize(image, (32, 32))  # Resize the image
    image = image.astype(np.float32) / 255.0  # Normalize pixel values
    images.append(image)

# Convert the image and label lists to NumPy arrays
images = np.array(images)
labels = np.array(labels)

# Splitting the Dataset
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Create a CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)
