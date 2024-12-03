# IoT Sensor Data Fault Detection

This repository contains the final project for **DS5110: Introduction to Data Management and Processing** at Khoury College of Computer Sciences, Northeastern University. The project focuses on detecting faults in IoT sensor data using deep learning techniques, enhancing data reliability, system efficiency, and operational safety in IoT-based systems.

---

## Project Overview

The Internet of Things (IoT) is a transformative technology connecting devices embedded with sensors to gather and transmit data across networks. While it has applications in healthcare, agriculture, and smart cities, the accuracy and reliability of IoT data are often compromised due to sensor malfunctions. This project addresses these challenges by employing advanced fault detection methodologies.

### Objectives
- Detect faults in IoT sensors to ensure data integrity and system reliability.
- Use deep learning models to classify faults and detect anomalies in sensor data.
- Enhance decision-making processes in real-world IoT environments.

---

## Methodology

### Data Collection
- **Dataset 1 (Real-World Data)**: Provided by an Indian private company, accessed securely via a private Kaggle notebook.
- **Dataset 2 (Synthetic Data)**: Generated using Python to complement the real-world dataset for testing preprocessing methods and refining models.

### Preprocessing Techniques
- **Normalization**: Min-max scaling to standardize sensor readings.
- **Data Augmentation**: Simulated variations such as rotations and brightness adjustments for improved model generalization.
- **Data Splitting**: 80-10-10 split for training, validation, and testing datasets.

### Models Used
1. **Convolutional Neural Networks (CNNs)**:
   - For fault classification using spatial and temporal patterns in sensor data.
2. **Autoencoders**:
   - For anomaly detection through reconstruction error.
3. **Long Short-Term Memory (LSTM)**:
   - For capturing temporal dependencies in time-series data.

---

## Experimental Setup
- Implemented using **Python 3.8** with libraries such as TensorFlow, Keras, and scikit-learn.
- Training conducted on Kaggle GPUs for efficiency.
- Visualization dashboards developed using **Streamlit**.

---

## Key Results
- **CNN Performance**:
  - Average training accuracy: 85%
  - Average validation accuracy: 84%
  - F1 Score: 82%
- **Autoencoder Effectiveness**:
  - Accurately detected anomalies with minimal false positives.
- **LSTM Integration**:
  - Improved fault detection for time-series data.

---

## Features
- Fault classification and anomaly detection using CNN and Autoencoder models.
- Preprocessing scripts for data normalization and augmentation.
- Visualization dashboards for real-time analysis of model performance.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/aryanshah295/Fault-Detection-in-IoT-Sensors.git
   cd Fault-Detection-in-IoT-Sensors
   ```

# Conclusion
This project demonstrates the potential of deep learning in improving IoT sensor reliability by effectively detecting faults and anomalies. The integration of real-world and synthetic data provided robust training and testing frameworks, making the models suitable for real-time IoT applications.

### Team Members
- **Aryan Shah**: shah.aryanr@northeastern.edu
- **Atir Shakhrelia**: shakhrelia.a@northeastern.edu
- **Jwal Shah**: shah.jwalp@northeastern.edu

