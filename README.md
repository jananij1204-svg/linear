#  Cafe Shop Sales Prediction using Linear Regression

This project analyzes cafe shop sales data and builds a **Linear Regression model** to predict **Total Sales** based on various features such as date-related factors, quantity sold, and other operational variables.

The goal is to understand **key drivers of revenue** and provide **actionable business insights** using machine learning.

---

##  Project Overview

* Performed **Exploratory Data Analysis (EDA)** on cafe sales data
* Engineered **date-based features** (day of year, week, quarter, etc.)
* Applied **feature scaling** and **feature selection**
* Built and evaluated a **Linear Regression model**
* Visualized results and interpreted model coefficients
* Saved the trained model and preprocessing objects for reuse

---

##  Technologies Used

* **Python**
* **Pandas & NumPy** – Data manipulation
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Machine learning
* **Joblib / Pickle** – Model persistence

---

##  Dataset

* Source: Excel file (`cafe_sales_dataset.xlsx`)
* Sheet used: `Cafe_Sales_Data`
* Target variable: **Total_Sales**

### Sample Features:

* Quantity Sold
* Day of Year
* Week of Year
* Quarter
* Other sales and operational features

---

##  Key Steps

### 1. Data Preprocessing

* Converted date columns to datetime format
* Created new time-based features
* Checked for missing values
* Selected relevant features for modeling

### 2. Feature Scaling & Selection

* Used **StandardScaler** for normalization
* Applied **SelectKBest (f_regression)** to select top features

### 3. Model Training

* Algorithm: **Linear Regression**
* Train-test split: **80% / 20%**

### 4. Model Evaluation

Metrics used:

* **R² Score**
* **RMSE**
* **MAE**
* **MAPE**

📈 The model achieved **high accuracy (R² > 0.94)** on both training and test data, showing strong generalization.

---

##  Visualizations

* Sales distribution histogram
* Feature correlation plots
* Heatmap of top correlated features
* Actual vs Predicted (Train & Test)
* Residuals plot
* Feature importance bar chart

---

##  Key Insights

* Coffee and food item sales are major revenue drivers
* Machine issues and poorly performing promotions negatively impact sales
* The model shows minimal overfitting
* Results are interpretable and business-friendly

---

##  Saved Files

The following files are generated after training:

* `cafe_sales_model.pkl` – Trained Linear Regression model
* `scaler.pkl` – StandardScaler
* `feature_selector.pkl` – Feature selector
* `cafe_sales_input.csv` – Model input features

---

##  How to Run

1. Clone the repository

```bash
git clone https://github.com/jananij1204-svg/Cafe-sales-linear-regression.git
```

2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

3. Run the Python script

```bash
python cafe_shop_sales_linear_regression_own1.py
```

---

##  Future Improvements

* Try advanced models (Ridge, Lasso, Random Forest)
* Hyperparameter tuning
* Handle outliers more robustly
* Deploy model using Flask or Streamlit

---

##  Streamlit App

An interactive **Streamlit web application** has been built on top of this model to allow users to predict cafe shop sales in real time.

🔗 **Live App:** [https://linear-2fp8hv9glafdvcek4mpdyq.streamlit.app/)

###  App Screenshots

#### App Home – CSV Upload

<img width="1920" height="1080" alt="Screenshot 2026-02-06 155406" src="https://github.com/user-attachments/assets/826acae2-1496-4738-92a7-1f79757483fa" />
<img width="1920" height="1080" alt="Screenshot 2026-02-06 155456" src="https://github.com/user-attachments/assets/4aa64fc4-f8bc-4e85-aa09-1096a350c6ef" />
<img width="1920" height="1080" alt="Screenshot 2026-02-06 155528" src="https://github.com/user-attachments/assets/75800bef-5bb4-491e-b72c-e9d8d78b6347" />

---

## 👤 Author

**Janani**
Machine Learning & Data Analysis Enthusiast
