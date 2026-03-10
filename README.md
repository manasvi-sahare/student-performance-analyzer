<img width="929" height="792" alt="image" src="https://github.com/user-attachments/assets/13cbb54e-5b91-403e-9389-b95ca16b91a0" />#  Student Performance Risk Analyzer

An interactive **data analysis and risk intelligence dashboard** built with **Python and Streamlit** to identify students at academic risk using interpretable, rule-based analytics.

The project combines **exploratory data analysis (EDA)**, **feature engineering**, and a **transparent risk scoring model** to help detect students who may require early academic intervention.

---

#  Project Overview

Academic performance is influenced by multiple factors such as:

- Study habits
- Attendance
- Past failures
- Family support

This project analyzes these factors and creates a **risk scoring system** that categorizes students into:

-  High Risk  
-  Medium Risk  
-  Low Risk  

The dashboard allows users to explore relationships between behavioral factors and student performance through interactive visualizations.

---

#  Key Features

##  Exploratory Data Analysis
Visual analysis of student behavior and performance:

- Absences vs Average Grade
- Study Time vs Average Grade
- Risk Level vs Academic Performance

---

##  Interpretable Risk Scoring Model

A weighted rule-based scoring system based on normalized factors:


Risk Score =
0.4 × Absence Risk

0.3 × Past Failures

0.2 × Study Time Risk

0.1 × Family Support Risk


This ensures the model is **transparent and explainable**.

---

##  Risk Categorization

Students are classified into risk groups:

| Risk Score | Category |
|------------|----------|
| ≥ 0.60 | High Risk |
| 0.35 – 0.59 | Medium Risk |
| < 0.35 | Low Risk |

---

##  Explainable Insights

For each high-risk student, the system identifies the **primary contributing factor**, such as:

- High Absences
- Past Academic Failures
- Low Study Time
- Lack of Family Support

---

##  Risk Model Validation

The system validates its predictions using the **final grade (G3)**.

It calculates the percentage of students classified as **High Risk** who actually scored below the passing threshold.

This provides **evidence that the risk scoring model is meaningful**.

---

##  What-If Analysis

Users can simulate improvements such as:

- reducing absences
- increasing study time
- adding family support

The dashboard recalculates the **new risk score** to show potential academic improvement.

---

#  Dataset

Dataset: **UCI Student Performance Dataset**

The dataset includes features such as:

- studytime
- absences
- failures
- family support
- grades (G1, G2, G3)

These features are used to build the risk analysis model.

---

#  Tech Stack

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Streamlit

---

#  How to Run the Project

## 1️. Clone the repository

```bash
git clone https://github.com/yourusername/student-performance-analyzer.git
cd student-performance-analyzer
2. Create virtual environment
python -m venv venv

Activate it:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
3️. Install dependencies
pip install streamlit pandas numpy matplotlib seaborn
4️. Run the dashboard
streamlit run app.py

The dashboard will open at:

http://localhost:8501
 Example Insights

Some insights discovered during analysis:

Students with high absences tend to have lower grades

Past failures strongly correlate with future academic risk

Higher study time improves performance stability

 Limitations

The risk model is rule-based, not machine learning based

Some socio-economic factors may introduce bias

The system is designed to assist educators, not replace human decision making

 Future Improvements

Possible extensions for this project:

Machine Learning risk prediction model

Student performance time-series tracking

Intervention recommendation system

Deployment on Streamlit Cloud

 Author

Manasvi Sahare

Data Science / Analytics Enthusiast

 This project demonstrates how interpretable analytics and visualization can help identify students who may benefit from early academic support.


---


##  Dashboard Preview
### Exploratory Data Analysis
![EDA] (images/EDA.png)
###  What_if_analysis
![What if analysis] (images/What if.png)
