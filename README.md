# 📊 Sales Performance & Revenue Analysis Dashboard

An end-to-end data analytics project designed to analyze sales performance, uncover revenue trends, and deliver business-ready insights using Python, SQL, and Excel.

This project mirrors a real-world analytics workflow followed by data analysts in business environments.

---

## 🔍 Project Overview

The objective of this project is to:
- Clean and preprocess raw sales data
- Analyze sales performance across products, regions, and time
- Validate insights using SQL
- Present findings through an interactive Excel dashboard

This project is suitable for **Data Analyst / Financial Analyst** roles and demonstrates practical analytics skills.

---

## 🛠 Tech Stack

- **Python**
- **Pandas, NumPy**
- **MySQL**
- **Excel (Pivot Tables, Charts, Slicers)**
- **Git & GitHub**

---

## 📁 Project Structure

Sales_Performance_Analysis/
│
├── dashboard/
│ └── Sales Performance Dashboard.xlsx
│
├── data/
│ ├── raw_sales_data.csv
│ └── cleaned_sales_data.csv
│
├── python/
│ ├── data_cleaning.py
│ ├── analysis.py
│ └── mysql_upload.py
│
├── sql/
│ └── sales_queries.sql
│
├── README.md
├── requirements.txt
└── .gitignore


---

## 🔄 Project Workflow

### 1️⃣ Data Cleaning (Python & Pandas)
- Loaded raw CSV sales data
- Removed duplicates and handled missing values
- Standardized date formats
- Generated cleaned dataset for analysis

📄 File: `python/data_cleaning.py`

---

### 2️⃣ Sales Analysis (Python & Pandas)
- Identified top-performing products
- Calculated region-wise revenue contribution
- Analyzed monthly and seasonal sales trends

📄 File: `python/analysis.py`

---

### 3️⃣ SQL Validation (MySQL)
- Uploaded cleaned data into MySQL using SQLAlchemy
- Validated Pandas-based insights with SQL queries
- Ensured data accuracy and consistency

📄 Files:
- `python/mysql_upload.py`
- `sql/sales_queries.sql`

---

### 4️⃣ Excel Dashboard
- Created an interactive Excel dashboard using Pivot Tables
- Visualized:
  - Revenue by Region
  - Sales by Product
  - Monthly Sales Trend
- Added slicers for business-friendly filtering

📄 File: `dashboard/Sales Performance Dashboard.xlsx`

---

## 📈 Key Business Insights

- Electronics category generated the highest revenue
- North region emerged as the top-performing region
- Sales showed clear monthly patterns indicating seasonality
- SQL results matched Python analysis, ensuring data reliability

---

## ▶️ How to Run the Project

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/sales-performance-analysis.git

2. Install dependencies:
pip install -r requirements.txt

3. Run data cleaning:
python python/data_cleaning.py

4. Run analysis:
python python/analysis.py

5. Upload data to MySQL:
python python/mysql_upload.py


---

## 🎯 Why This Project Matters

- Demonstrates end-to-end analytics workflow
- Combines Python, SQL, and Excel — industry-relevant tools
- Focuses on business insights, not just code
- Recruiter- and interview-friendly structure

---

## 👤 Author

**Dibyajyoti Roy**  
Aspiring Data / Financial Analyst  
Skilled in Python, Pandas, SQL, Excel, and Data Visualization


