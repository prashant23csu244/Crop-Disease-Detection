# 🌱 AI-Based Crop Disease Detection System Using Deep Learning

## 📌 Project Overview

This project uses Deep Learning and Convolutional Neural Networks (CNN) to detect crop diseases from leaf images. The system allows users to upload a crop leaf image through a Streamlit web application and receive:

- Disease Prediction
- Confidence Score
- Treatment Suggestions

The goal of this project is to help farmers identify plant diseases quickly and accurately, reducing crop losses and improving agricultural productivity.

---

## 🚀 Features

- Upload crop leaf images
- Automatic disease detection using CNN
- Confidence score display
- Treatment recommendations
- User-friendly Streamlit web interface
- Fast and accurate predictions

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- Google Colab
- NumPy
- Pillow

---

## 📂 Dataset

**PlantVillage Dataset**

- 54,000+ leaf images
- 38 disease classes
- Multiple crop species
- Healthy and diseased leaf samples

---

## 🧠 Model Architecture

The project uses a Convolutional Neural Network (CNN) trained on the PlantVillage dataset.

### Workflow

1. Upload Leaf Image
2. Image Preprocessing
3. CNN Prediction
4. Disease Detection
5. Confidence Score Generation
6. Treatment Suggestion Display

---

## 📁 Project Structure

```text
Crop-Disease-Detection/
│
├── app.py
├── class_names.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│
├── report/
│   └── Crop_Disease_Detection_Report.docx
│
└── model/
    └── crop_disease_model.h5
```

---

## 📥 Model Download

The trained model file is not included in this repository because GitHub has file size limitations.

Download the trained model from:

https://drive.google.com/file/d/1LhCVaFkRyNkztcuuNSR0neFn9vwwUMKN/view?usp=sharing

After downloading:

1. Create a folder named `model`
2. Place the downloaded file inside the folder
3. Rename the file to:

```text
crop_disease_model.h5
```

Final structure:

```text
model/
└── crop_disease_model.h5
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd Crop-Disease-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

## 📸 Screenshots

Add project screenshots inside the `screenshots` folder.

Examples:

- Home Page
- Disease Prediction Result
- System Architecture
- Accuracy Graph

---

## 📈 Future Scope

- Mobile Application Development
- Real-Time Camera Detection
- Multi-Language Support
- Drone-Based Disease Monitoring
- Cloud Deployment
- Expanded Crop Disease Dataset

---

## 🎯 Advantages

- Fast Disease Detection
- High Accuracy
- Easy to Use
- Cost Effective
- Helps Farmers Make Quick Decisions

---

## 📄 Project Report

The complete project report is available in:

```text
report/Crop_Disease_Detection_Report.docx
```

---

## 👨‍💻 Author
Prashant Kumar , Prateek Khatana

AI-Based Crop Disease Detection System Using Deep Learning

---

## 📜 License

This project is developed for educational and academic purposes.
