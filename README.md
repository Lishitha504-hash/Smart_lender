# 🏦 Smart Lender – AI-Powered Loan Approval Prediction

## 📌 Overview

**Smart Lender** is a Machine Learning-based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on an applicant's financial and personal details.

The application uses a **Random Forest Classifier** trained on historical loan data and displays the prediction, confidence score, probabilities, and decision factors through an interactive dashboard.

---

## 🚀 Features

- AI-based loan approval prediction
- Interactive web dashboard
- Random Forest classification model
- Prediction confidence score
- Approval and rejection probabilities
- Decision factors
- Approved and rejected sample inputs
- Responsive user interface

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Random Forest Classifier
- **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn, Plotly
- **Model Development:** Imbalanced-learn, XGBoost, LightGBM, Joblib

---

## 📂 Project Structure

```text
Smart-Lender/
│
├── data/
│   └── loan_prediction.csv
├── models/
│   ├── loan_model.pkl
│   └── feature_names.json
├── notebooks/
│   └── eda.ipynb
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── screenshots/
│   ├── approved.png
│   ├── rejected.png
│   └── dashboard.png
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Smart-Lender
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## 📊 Input Features

The model uses the following applicant details:

- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Number of Dependents
- Education
- Employment Type
- Residential Assets
- Commercial Assets
- Luxury Assets
- Bank Assets

---

## 🤖 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Library:** Scikit-learn
- **Number of Features:** 11
- **Accuracy:** **98.13%**

The trained model is stored in the `models/` directory and is used by the Flask application to generate predictions.

---

## 📈 Output

The application provides:

- Loan Approval or Rejection status
- Prediction confidence
- Approval probability
- Rejection probability
- Decision factors
- Model information

---

## 📷 Application Screenshots

### ✅ Approved Loan Prediction

<img width="1366" height="768" alt="Approved Loan Prediction" src="https://github.com/user-attachments/assets/cecf677f-c758-445f-bbfe-148c5101baaa" />

### ❌ Rejected Loan Prediction

<img width="1366" height="768" alt="Rejected Loan Prediction" src="https://github.com/user-attachments/assets/ff4a9bd2-9ad7-41d6-b80c-e0af700007af" />

### 📊 Smart Lender Dashboard

<img width="1366" height="768" alt="Smart Lender Dashboard" src="https://github.com/user-attachments/assets/2561e901-141b-42b5-adf8-798b9501399a" />

---

## 👥 Team Members

- Kamineni Lishitha
- Team Member 2
- Team Member 3
- Team Member 4

---

## 🔮 Future Enhancements

- User authentication
- Loan eligibility recommendations
- PDF report generation
- Database integration
- Model retraining with new data
- Cloud deployment

---

## 📄 License

This project is developed for educational purposes.



