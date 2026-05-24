# 🧠 Brain Tumor Detection Using CNN & Flask

A Deep Learning based Brain Tumor Detection Web Application built using 
**Convolutional Neural Networks (CNN)** and **Flask**.

The model classifies MRI brain scan images into:

- ✅ Healthy Brain
- ❌ Brain Tumor Detected

---

# 📚 Learning Outcomes

✔️ Image Classification  
✔️ MRI Image Processing  
✔️ Convolutional Neural Networks (CNN)  
✔️ Flask Web Development  
✔️ Medical Image Prediction System  

---

# 🧠 About CNN

CNN (Convolutional Neural Network) is a Deep Learning algorithm mainly used for:

- Image Classification
- Medical Imaging
- Pattern Recognition
- Object Detection

CNN automatically learns important features from MRI images like:
- edges
- textures
- abnormal tumor regions

---

# 📂 Dataset Used

Dataset Source:

[Kaggle Brain Tumor Dataset](https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset)

Dataset contains:
- Healthy Brain MRI Images
- Brain Tumor MRI Images

---

# 📁 Project Structure

```bash
brain_tumor_detection/
│
├── dataset/
│   ├── Healthy/
│   └── Brain Tumor/
│
├── static/
│   ├── style.css
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── BrainTumorDetection.ipynb
├── app.py
├── brain_tumor_model.h5
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- Flask
- HTML
- CSS

---


## Install Dependencies

```bash
pip install -r requirements.txt
```
---

# 🧠 CNN Model Architecture

Architecture Flow:

```text
Input Image
      ↓
Convolution Layer
      ↓
MaxPooling Layer
      ↓
Flatten Layer
      ↓
Dense Layer
      ↓
Output Prediction
```

---

# 📊 Model Training

Model trained using:
- Adam Optimizer
- Categorical Crossentropy Loss
- EarlyStopping Callback


# 💾 Save Trained Model

```python
model.save("brain_tumor_model.h5")
```

---

# 🌐 Flask Web Application

Run Flask App:

```bash
python app.py
```

Open Browser:

```text
http://127.0.0.1:5000
```

--- 

# 👩‍💻 Author

## Mokshada Patil

Data Science Engineering Student

Interested in:
- Deep Learning
- Medical AI
- Data Analytics
- Healthcare Technology

---
