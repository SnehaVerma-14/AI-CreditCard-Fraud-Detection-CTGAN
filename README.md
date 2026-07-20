# 💳 AI-Powered Credit Card Fraud Detection using CTGAN-Based Synthetic Data Generation

> **An AI/ML Internship Project completed at GNCIPL**
> Leveraging **Generative AI (CTGAN)** to address class imbalance in credit card fraud detection and improve machine learning model performance.

---

## 📌 Project Overview

Credit card fraud detection is a challenging classification problem due to the highly imbalanced nature of transaction data. Fraudulent transactions represent only a tiny fraction of all transactions, causing traditional machine learning models to favor legitimate transactions and miss fraudulent ones.

This project solves the class imbalance problem using **Conditional Tabular Generative Adversarial Networks (CTGAN)**, a Generative AI technique that learns the distribution of fraudulent transactions and generates realistic synthetic fraud samples.

The generated synthetic data is merged with the original dataset to create an augmented dataset, which is then used to train and evaluate machine learning models.

---

## 🎯 Objectives

* Detect fraudulent credit card transactions using Machine Learning.
* Generate realistic synthetic fraud transactions using CTGAN.
* Reduce dataset imbalance through data augmentation.
* Compare the performance of Random Forest and XGBoost.
* Evaluate models using standard classification metrics.

---

## 🚀 Key Features

* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Feature Scaling
* Fraud Data Extraction
* Synthetic Data Generation using CTGAN
* Dataset Augmentation
* Random Forest Classifier
* XGBoost Classifier
* Model Performance Comparison
* Feature Importance Analysis
* Model Saving using Joblib

---

## 🛠️ Technologies Used

| Category                | Technologies           |
| ----------------------- | ---------------------- |
| Programming Language    | Python                 |
| Development Environment | Google Colab           |
| Data Analysis           | Pandas, NumPy          |
| Visualization           | Matplotlib, Seaborn    |
| Machine Learning        | Scikit-learn           |
| Generative AI           | CTGAN (SDV Library)    |
| Classification Models   | Random Forest, XGBoost |
| Model Serialization     | Joblib                 |
| Version Control         | Git & GitHub           |

---

## 📂 Project Structure

```text
AI-CreditCard-Fraud-Detection-CTGAN/
│
├── notebook/
│   └── AI_CreditCard_Fraud_CTGAN.ipynb
│
├── data/
│   ├── fraud_data.csv
│   ├── synthetic_fraud_data.csv
│   └── augmented_dataset.csv
│
├── images/
│   ├── class_distribution.png
│   ├── amount_histogram.png
│   ├── time_histogram.png
│   ├── correlation_heatmap.png
│   ├── boxplot.png
│   ├── comparison_graph.png
│   ├── feature_importance.png
│   ├── rf_confusion_matrix.png
│   └── xgb_confusion_matrix.png
│
├── model/
│   └── fraud_detection_model.pkl
│
├── presentation/
│   └── AI_CreditCard_Fraud_CTGAN_Presentation.pptx
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**Dataset:** Credit Card Fraud Detection Dataset

**Source:** Kaggle

### Dataset Characteristics

* Total Transactions: **284,807**
* Fraudulent Transactions: **492**
* Features: **31**
* Target Column: **Class**

  * 0 → Legitimate Transaction
  * 1 → Fraudulent Transaction

> **Note:** The original dataset is not included in this repository because it is publicly available on Kaggle.

---

## 🔄 Project Workflow

```text
Credit Card Dataset
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Preprocessing
        │
        ▼
Extract Fraud Transactions
        │
        ▼
Train CTGAN Model
        │
        ▼
Generate Synthetic Fraud Data
        │
        ▼
Create Augmented Dataset
        │
        ▼
Train Random Forest
        │
        ▼
Train XGBoost
        │
        ▼
Evaluate Performance
        │
        ▼
Fraud Prediction
```

---

## 📈 Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

---

## 🖼️ Project Screenshots

### Dataset Distribution

> Add image:
>
> `images/class_distribution.png`

---

### Correlation Heatmap

> Add image:
>
> `images/correlation_heatmap.png`

---

### Random Forest Confusion Matrix

> Add image:
>
> `images/rf_confusion_matrix.png`

---

### XGBoost Confusion Matrix

> Add image:
>
> `images/xgb_confusion_matrix.png`

---

### Model Performance Comparison

> Add image:
>
> `images/comparison_graph.png`

---

### Feature Importance

> Add image:
>
> `images/feature_importance.png`

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-CreditCard-Fraud-Detection-CTGAN.git
```

Navigate to the project directory:

```bash
cd AI-CreditCard-Fraud-Detection-CTGAN
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook using Google Colab or Jupyter Notebook.

---

## 💡 Future Enhancements

* Real-time fraud detection
* Web application deployment using Flask/FastAPI
* Explainable AI (SHAP/LIME)
* Deep Learning-based fraud detection
* Cloud deployment
* Integration with banking systems
* Continuous model retraining

---

## 👩‍💻 Author

**Sneha Verma**

B.Tech – Computer Science (Artificial Intelligence)

Noida Institute of Engineering and Technology (NIET)

AI/ML Internship – GNCIPL

---

## 📜 License

This project is developed for educational and internship purposes.
