# 🚀 AI-Powered Predictive Maintenance System for IoT Devices

## 📌 Overview

This project is an end-to-end AI system that predicts machine failures using IoT sensor data such as temperature, vibration, and pressure.

It helps industries detect potential issues before breakdowns occur, reducing downtime and maintenance costs.

---

## 🎯 Objective

To build a predictive maintenance system that analyzes sensor data and predicts machine failure using Machine Learning and Deep Learning techniques.

---

## 🧠 Features

* Machine Learning model (Random Forest)
* Deep Learning model (LSTM)
* Data preprocessing and normalization
* Model evaluation (Accuracy, Confusion Matrix)
* Flask API for real-time prediction
* Web UI for user input
* Data visualization (graphs)

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* TensorFlow / Keras
* Flask
* Matplotlib

---

## 📁 Project Structure

```
AI-Predictive-Maintenance-IoT/
│
├── app.py
├── main.py
├── train_lstm_model.py
├── predict.py
├── preprocess.py
├── data_loader.py
├── visualize.py
│
├── models/
├── data/
├── templates/
│
├── confusion_matrix.png
├── temperature.png
│
├── README.md
├── requirements.txt
```

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train ML model

```
python main.py
```

### 3. Train LSTM model

```
python train_lstm_model.py
```

### 4. Run Flask App

```
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 📊 Results

* Random Forest Accuracy: ~99%
* LSTM Accuracy: ~85%
* Successfully predicts machine failure

---

## 🌐 API Example

POST request:

```
http://127.0.0.1:5000/predict
```

JSON Input:

```
{
  "temperature": 85,
  "vibration": 5,
  "pressure": 30
}
```

---

## 💡 Industry Use Cases

* Manufacturing plants
* Power plants
* Automotive industry
* Industrial IoT systems

---

## 🙏 Acknowledgment

Special thanks to my mentor Umesh Yadav sir for guidance and support.

---

## 👨‍💻 Author

Jatin Gujarathi

---

## ⭐ If you like this project, please give it a star!
