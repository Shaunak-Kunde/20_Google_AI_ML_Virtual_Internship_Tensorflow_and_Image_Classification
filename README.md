📌 AI/ML – Google EduSkills AICTE Internship

📅 Date: 12-08-2025
🎓 ME Data Science – Semester 3
🏢 Google EduSkills AICTE Internship Task
🇮🇳 India

✅ Project Overview

This notebook covers two major components from the Intro to TensorFlow and Computer Vision modules.
The objective is to demonstrate the complete workflow of:

✅ Building and training neural networks

✅ Document retrieval using Vector Space Model

✅ Applying TF-IDF and Cosine Similarity

✅ Deep learning model development with real datasets

✅ Computer Vision classification using Fashion MNIST

🔍 Module 1 — Machine Learning Introduction

A single-layer neural network (Dense Linear Regression Model) was implemented using TensorFlow Keras:

✔ Key Steps:

Model: Dense(units=1)

Loss: Mean Squared Error

Optimizer: Stochastic Gradient Descent (SGD)

Training Data:

Input: xs = [-1, 0, 1, 2, 3, 4]

Target: ys = [-2, 1, 4, 7, 10, 13]

Epochs: 50

📈 Model Inference:

Input = 10 → Output ≈ 31.09

👁️ Module 2 — Computer Vision with TensorFlow

Dataset used: Fashion MNIST

✔ Workflow:

Dataset loading and sample visualization

Pixel normalization for faster convergence

Model training and performance measurement

✔ Model Architecture:
Flatten → Dense(128, ReLU) → Dense(10, Softmax)

✔ Performance:

Loss: Sparse Categorical Crossentropy

Optimizer: Adam

Epochs: 5
✅ Achieved ~78–80% accuracy

📚 Information Retrieval System (IRS)

Complete Document Search Pipeline implemented:

Stage	Status	Method
Document Input	✅	Local .docx files
Preprocessing	✅	Text cleanup & merging
Feature Extraction	✅	TF-IDF
Vector Representation	✅	Vector Space Model
Similarity Ranking	✅	Cosine Similarity
Output Retrieval	✅	Top matching document

Result: Most relevant document returned for user queries.

🛠️ Tech Stack
Category	Tools
Code	Python
Deep Learning	TensorFlow, Keras
NLP & IR	TF-IDF, Cosine Similarity
Visualization	Matplotlib
Dataset	Fashion MNIST
📎 Skills Demonstrated

✅ Linear regression using DL models
✅ Neural network training and prediction
✅ Computer Vision classification
✅ Information retrieval concepts
✅ TF-IDF vectorization + Cosine similarity scoring
✅ ML model evaluation & visualizations

🙌 Acknowledgement

Developed as part of:
Google EduSkills AI-ML Internship Program
(Approved by AICTE)
