# 💳 Credit Card Fraud Detection using Machine Learning

## 📌 Project Overview

Credit card fraud has become a significant challenge in the financial industry due to the increasing number of online transactions. Detecting fraudulent transactions accurately while minimizing false alarms is essential for protecting customers and financial institutions.

This project develops a **Machine Learning-based Credit Card Fraud Detection System** by training and evaluating multiple classification algorithms on a balanced dataset. Various models were compared using multiple evaluation metrics, and the best-performing model was selected for deployment.

---

# 📂 Project Structure

```
credit_card_detection/
│
├── dataset/
│   ├── creditcard.csv
│   └── creditcard_balanced.csv
│
├── model/
│   └── logistic_regression.pkl
│
├── notebook/
│   └── credit_card_fraud_detection.ipynb
│
├── requirements.txt
├── README.md

```

---

# 📊 Dataset

Dataset contains anonymized credit card transactions.

Features:

- Time
- V1 – V28 (PCA transformed features)
- Amount
- Class

Target Variable:

- **0 → Normal Transaction**
- **1 → Fraudulent Transaction**

Since the original dataset is highly imbalanced, a balanced dataset was created using random sampling before model training.

---

# 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Dataset Overview
- Missing Value Check
- Duplicate Record Check
- Class Distribution Analysis
- Data Balancing
- Feature & Target Separation
- Train-Test Split

---

# ⚙️ Data Preprocessing

- Balanced the dataset
- Shuffled the dataset
- Feature-Target Separation
- Train-Test Split
- Feature Scaling (for applicable algorithms)

---

# 🤖 Machine Learning Models

The following classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gaussian Naive Bayes
- Random Forest

---

# 🎯 Hyperparameter Tuning

GridSearchCV was used to optimize the following models:

- Logistic Regression
- Decision Tree
- KNN
- SVM
- Random Forest

---

# 🤝 Ensemble Learning

Implemented ensemble techniques:

### Voting Classifier

- Hard Voting
- Soft Voting

### Bagging Classifier

Bagging was implemented using Decision Trees with different numbers of estimators.

---

# 📈 Model Performance Comparison

The performance of each machine learning model was evaluated using **Accuracy, Precision, Recall, and F1-Score** before and after hyperparameter tuning.

| Model | Default Accuracy | Tuned Accuracy | Default Precision | Tuned Precision | Default Recall | Tuned Recall | Default F1-Score | Tuned F1-Score |
|------|:----------------:|:--------------:|:-----------------:|:---------------:|:--------------:|:------------:|:----------------:|:--------------:|
| Logistic Regression | 95.26% | **95.26%** | 98.95% | 97.94% | 92.16% | **93.14%** | 95.43% | **95.48%** |
| Decision Tree | 95.26% | 93.16% | 98.95% | 93.20% | 92.16% | 94.12% | 95.43% | 93.66% |
| K-Nearest Neighbors | 91.05% | 92.11% | 96.70% | 96.77% | 86.27% | 88.24% | 91.19% | 92.31% |
| Support Vector Machine | 94.74% | **95.26%** | 98.94% | 98.95% | 91.18% | 92.16% | 94.90% | 95.43% |
| Gaussian Naive Bayes | 91.58% | — | 97.78% | — | 86.27% | — | 91.67% | — |
| Random Forest | 93.16% | 94.74% | 94.06% | 97.92% | 93.14% | 92.16% | 93.60% | 94.95% |
| Hard Voting | **95.26%** | — | 98.95% | — | 92.16% | — | 95.43% | — |
| Soft Voting | 94.74% | — | 98.94% | — | 91.18% | — | 94.90% | — |
| Bagging | 93.68% | 94.74% | 95.92% | 96.94% | 92.16% | 93.14% | 95.00% | 95.00% |

> **Final Selected Model:** **Tuned Logistic Regression**  
> It achieved the best balance of **Accuracy (95.26%)**, **Recall (93.14%)**, and **F1-Score (95.48%)**, making it the most suitable model for credit card fraud detection.
---

# 🏆 Final Model Selection

After evaluating all machine learning models, **Tuned Logistic Regression** was selected as the final model.

### Reasons for Selection

- Highest F1-Score
- Excellent Accuracy (95.26%)
- High Precision (97.94%)
- High Recall (93.14%)
- Computationally efficient
- Easy to interpret
- Suitable for real-world deployment

The trained model was serialized using **Pickle** for future prediction and deployment.

---

# 💾 Saved Model

```
model/logistic_regression.pkl
```

---

# 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- Jupyter Notebook

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Rupesh-Mane/credit-card-fraud-detection.git
```

Move into the project

```bash
cd credit-card-fraud-detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

---

# 📌 Future Improvements

- ROC Curve & AUC Score Comparison
- Precision-Recall Curve
- Cross Validation Analysis
- XGBoost
- LightGBM
- CatBoost
- Model Deployment using FastAPI
- Docker Containerization

---

# 👨‍💻 Author

**Rupesh Mane**

---

# ⭐ If you found this project useful, consider giving it a star!