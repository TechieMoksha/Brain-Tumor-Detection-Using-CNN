from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)

# Load Trained Model
model = tf.keras.models.load_model("brain_tumor_model.h5")

# Upload Folder
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Categories
categories = ["Healthy", "Brain Tumor"]

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return "No File Uploaded"

    file = request.files['image']

    if file.filename == '':
        return "No Selected File"

    # Save Uploaded Image
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(file_path)

    # Read Image
    img = cv2.imread(file_path)

    # Resize Image
    img = cv2.resize(img, (128, 128))

    # Normalize
    img = img / 255.0

    # Reshape
    img = np.reshape(img, [1, 128, 128, 3])

    # Prediction
    prediction = model.predict(img)

    result = np.argmax(prediction)

    label = categories[result]

    # Final Result Text
    if label == "Brain Tumor":
        result_text = "Brain Tumor Detected"
    else:
        result_text = "No Brain Tumor Detected"

    return render_template(
        'index.html',
        prediction=result_text,
        image_path='/' + file_path
    )

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)