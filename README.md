# 🚗 Vehicle Damage Detection using Deep Learning

An end-to-end Deep Learning application that classifies vehicle damage from images using **Transfer Learning with ResNet50**. The project includes a **Streamlit web application** that enables users to upload vehicle images and receive instant damage classification predictions.

---

## 📌 Project Overview

Vehicle damage assessment is a critical task in the automotive and insurance industries. This project leverages Deep Learning and Transfer Learning to automate the classification of vehicle damage into six categories based on the location and severity of the damage.

The final deployed model uses **ResNet50**, fine-tuned on a custom vehicle damage dataset and integrated into an interactive Streamlit application.

---

## 🚀 Features

- Deep Learning image classification using **ResNet50**
- Transfer Learning with ImageNet pretrained weights
- Real-time prediction through a **Streamlit** web application
- Automatic image preprocessing and normalization
- Hyperparameter tuning for model optimization
- Performance evaluation using Classification Report and Confusion Matrix
- Clean and modular project structure

---

## 🧠 Damage Categories

The model classifies vehicle images into one of the following categories:

- Front Breakage
- Front Crushed
- Front Normal
- Rear Breakage
- Rear Crushed
- Rear Normal

---

## 🛠️ Technologies Used

- Python
- PyTorch
- Torchvision
- Streamlit
- NumPy
- Scikit-learn
- Matplotlib
- Pillow

---

## 📂 Project Structure

```text
vehicle-damage-detection/
│
├── model/
│   └── saved_model.pth
│
├── notebooks/
│   ├── damage_prediction.ipynb
│   └── hyperparameter_tuning.ipynb
│
├── screenshots/
│   └── app_screenshot.jpg
│
├── app.py
├── model_helper.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🏗️ Model Development

Multiple Deep Learning models were trained and evaluated before selecting the final model:

- Custom CNN
- CNN with Regularization
- EfficientNet-B0
- **ResNet50 (Final Model)**

### Final Model Configuration

- Architecture: **ResNet50**
- Transfer Learning (ImageNet pretrained)
- Dropout: **0.2**
- Optimizer: **Adam**
- Learning Rate: **0.005**
- Loss Function: **CrossEntropyLoss**

---

## 📊 Model Performance

The final ResNet50 model achieved approximately:

- **Validation Accuracy:** ~79%

Evaluation metrics include:

- Classification Report
- Confusion Matrix

---

## 📸 Application Screenshot

![Vehicle Damage Detection](screenshots/app_screenshot.jpg)

---

## 💻 Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/vehicle-damage-detection.git
```

### 2. Navigate to the project directory

```bash
cd vehicle-damage-detection
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

---

## 📁 Dataset

The dataset contains vehicle images categorized into six classes representing different damage locations and conditions.

> **Note:** The dataset is not included in this repository due to its size. Place the dataset in the project directory following the folder structure used during training.

---

## 🔮 Future Improvements

- Object detection using YOLO
- Damage localization with bounding boxes
- Damage severity estimation
- Support for additional vehicle types
- Model optimization for mobile deployment
- Larger and more diverse training dataset

---

## 👨‍💻 Author

**George P Alex**

Aspiring Data Scientist | Machine Learning & Deep Learning Enthusiast

- GitHub: https://github.com/Georgepalex

---

### ⭐ If you found this project useful, consider giving it a Star!
