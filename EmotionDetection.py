import cv2 as cv
import numpy as np
import os
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Define emotion labels
emotion_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral', 'Contempt']

# Load and preprocess data
path = r"A:\New folder"
data = []
y = []

for i, dir_name in enumerate(os.listdir(path)):
    dir_path = os.path.join(path, dir_name)
    
    if os.path.isdir(dir_path):
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            img = cv.imread(file_path, cv.IMREAD_GRAYSCALE)
            
            if img is not None:
                img = cv.resize(img, (28, 28))
                img = img / 255.0
                
                data.append(img)
                y.append(i)

data = np.array(data)
y = np.array(y)

X = np.expand_dims(data, axis=3)
y = tf.keras.utils.to_categorical(y, 8)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training Data shape: {X_train.shape}")
print(f"Training Labels shape: {y_train.shape}")
print(f"Testing Data shape: {X_test.shape}")
print(f"Testing Labels shape: {y_test.shape}")

# Define and compile the model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, kernel_size=3, padding="same", activation="relu", input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Conv2D(64, kernel_size=3, padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Conv2D(128, kernel_size=3, padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(8, activation="softmax")
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss="categorical_crossentropy",
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100, validation_split=0.2)

model.summary()
loss, acc = model.evaluate(X_test, y_test)
print(f"Accuracy: {acc*100:.2f}%")

# Capture video and make predictions
cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Preprocess the frame
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Convert to grayscale
        img = cv.resize(img, (28, 28))  # Resize to 28x28
        img = img / 255.0  # Normalize
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        img = np.expand_dims(img, axis=3)  # Add channel dimension

        # Make prediction
        yhat = model.predict(img)
        label_idx = np.argmax(yhat)  # Get the index of the highest probability
        label_text = emotion_labels[label_idx]  # Convert index to emotion label

        # Display the prediction on the frame
        cv.putText(frame, f'Predicted Emotion: {label_text}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv.destroyAllWindows()
