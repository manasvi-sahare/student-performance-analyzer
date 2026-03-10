# import streamlit as st
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt


# st.set_page_config(
#     page_title="Student Performance Risk Analyzer",
#     layout="wide"
# )

# st.title("Student Performance EDA & Risk Analyzer")
# st.write(
#     "An interpretable, rule-based academic risk analysis system with validation and what-if insights."
# )

# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/student.csv",sep=';')

#     df["avg_grade"] = df[["G1", "G2", "G3"]].mean(axis=1)
#     df["famsup_num"] = df["famsup"].map({"yes":1,"no":0})
#     df["study_score"] = df["studytime"]*2
#     df["attendance_score"] = np.where(
#         df["absences"]<5,10,
#         np.where(df["absences"]<10,5,0)
#     )
#     df["failure_penalty"] = df["failures"]* -5
#     df["risk_score"] = (
#         df["study_score"]
#         + df["attendance_score"]
#         + df["failure_penalty"]
#         + df["famsup_num"]*2
#     )

#     def categorize_risk(score):
#         if score <= 5:
#             return "High Risk"
#         elif score <= 10:
#             return "Medium Risk"
#         else:
#             return "Low Risk"

#     df["risk_level"] = df["risk_score"].apply(categorize_risk)

#     return df

# df = load_data()

# st.subheader("Key Insights")
# col1,col2,col3 = st.columns(3)

# with col1:
#     st.metric("Total Students",len(df))

# with col2:
#     st.metric("High Risk Students",(df["risk_level"] =="High Risk").sum())

# with col3:
#     st.metric("Average Grade",
#               round(df["avg_grade"].mean(),2))

# st.sidebar.header("Filters")
# risk_filter = st.sidebar.radio(
#     "Select Risk Level",
#     options=["All", "High Risk", "Medium Risk", "Low Risk"]
# )

# if risk_filter != "All":
#     filtered_df = df[df["risk_level"]==risk_filter]
# else:
#     filtered_df = df.copy()

# st.subheader("Exploratory Data Analysis")

# col1,col2 = st.columns(2)
# with col1:
#     st.write("**Absences vs Average Grade**")
#     fig1, ax1 = plt.subplots()
#     sns.scatterplot(
#         data = filtered_df,
#         x = "absences",
#         y = "avg_grade",
#         hue = "risk_level",
#         ax = ax1
#     )
#     st.pyplot(fig1)

# with col2:
#     st.write("**Study Time vs Average Grade**")
#     fig2, ax2 = plt.subplots()
#     sns.boxplot(
#         data = filtered_df,
#         x = "studytime",
#         y = "avg_grade",
#         hue = "risk_level",
#         ax = ax2
#     )
#     st.pyplot(fig2)

# st.subheader(" RISK LEVEL VS PERFORMANCE")

# fig3,ax3 = plt.subplots()
# sns.boxplot(
#     data = filtered_df,
#     x = "risk_level",
#     y = "avg_grade",
#     order = ["High Risk","Medium Risk","Low Risk"],
#     ax = ax3
# )
# st.pyplot(fig3)

# st.subheader("High-Risk Students")

# high_risk = df[df["risk_level"] == "High Risk"]

# st.dataframe(
#     high_risk[
#         ["studytime", "absences", "failures", "avg_grade", "risk_score"]
#     ]
# )

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Student Performance Risk Analyzer",
    layout="wide"
)

st.title("Student Performance EDA & Risk Analyzer")
st.write(
    "An interpretable, rule-based academic risk analysis system with validation and what-if insights."
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/student.csv", sep=';')

    # Core features
    df["avg_grade"] = df[["G1", "G2", "G3"]].mean(axis=1)
    df["famsup_num"] = df["famsup"].map({"yes": 0, "no": 1})

    # Normalized risk components
    df["abs_norm"] = df["absences"] / df["absences"].max()
    df["fail_norm"] = df["failures"] / (df["failures"].max() or 1)  # <- fixed here
    df["study_norm"] = 1 - (df["studytime"] / df["studytime"].max())

    # Weighted risk score
    df["risk_score"] = (
        0.4 * df["abs_norm"] +
        0.3 * df["fail_norm"] +
        0.2 * df["study_norm"] +
        0.1 * df["famsup_num"]
    )

    # Risk categorization
    def categorize_risk(score):
        if score >= 0.6:
            return "High Risk"
        elif score >= 0.35:
            return "Medium Risk"
        else:
            return "Low Risk"

    df["risk_level"] = df["risk_score"].apply(categorize_risk)
    df["actual_low_perf"] = df["G3"] < 10

    # Primary risk reason
    factors = ["abs_norm", "fail_norm", "study_norm", "famsup_num"]
    df["top_factor"] = df[factors].idxmax(axis=1)
    reason_map = {
        "abs_norm": "High Absences",
        "fail_norm": "Past Academic Failures",
        "study_norm": "Low Study Time",
        "famsup_num": "Lack of Family Support"
    }
    df["primary_risk_reason"] = df["top_factor"].map(reason_map)

    return df



df = load_data()

st.sidebar.header("Filters")
risk_filter = st.sidebar.radio(
    "Select Risk Level",
    options = ["All" , "High Risk", "Medium Risk" , "Low Risk"]
)

if risk_filter != "All":
    filtered_df = df[df["risk_level"] == risk_filter]
else:
    filtered_df = df.copy()

st.subheader("Key Metrics")
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Total Students",len(df))

with col2:
    st.metric("High Risk Students", (df["risk_level"] == "High Risk").sum())

with col3:
    st.metric("Average Final Grade", round(df["G3"].mean(),2))

with col4:
    high_risk = df[df["risk_level"] == "High Risk"]
    validation_acc = high_risk["actual_low_perf"].mean()*100
    st.metric("High Risk Validation", f"{validation_acc:.1f}%")

st.subheader("Exploratory Data Analysis")

col1,col2 = st.columns(2)

with col1:
    st.write("**Absences vs Average Grade**")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(
        data = filtered_df,
        x = "absences",
        y = "avg_grade",
        hue = "risk_level",
        ax = ax1
    )
    st.pyplot(fig1)

with col2:
    st.write("**Study Time vs Average Grade**")
    fig2, ax2 = plt.subplots()
    sns.boxplot(
        data = filtered_df,
        x = "studytime",
        y = "avg_grade",
        hue = "risk_level",
        ax = ax2
    )
    st.pyplot(fig2)

st.subheader("Risk Level vs Academic Performance")
fig3, ax3 = plt.subplots()
sns.boxplot(
    data = filtered_df,
    x = "risk_level",
    y = "avg_grade",
    order = ["High Risk", "Medium Risk", "Low Risk"],
    ax = ax3
)
st.pyplot(fig3)

st.subheader("High Risk Students Analysis")
st.dataframe(
    df[df["risk_level"] == "High Risk"][[
        "studytime",
        "absences",
        "failures",
        "avg_grade",
        "risk_score",
        "primary_risk_reason"
    ]].sort_values("risk_score",ascending=False)
)

st.subheader("What-If Analysis (Single Student)")
selected_index = st.selectbox("Slect Student Index",df.index)
student = df.loc[selected_index]

new_absences = st.slider("Reduce Absences",0,int(student.absences),int(student.absences))
new_studytime = st.slider("Increase Study Time", 1, 4, int(student.studytime))
new_famsup = st.radio("Family Support", ["yes","no"], index = 0 if student.famsup_num == 0 else 1)
abs_norm = new_absences / df["absences"].max()
study_norm = 1 - (new_studytime / df["studytime"].max())
fam_norm = 0 if new_famsup == "yes" else 1
fail_norm = student.fail_norm

new_risk = 0.4*abs_norm + 0.3*fail_norm + 0.2*study_norm + 0.1*fam_norm

st.write(f"**Original Risk Score:** {student.risk_score:.2f} ({student.risk_level})")
st.write(f"**New Risk Score:** {new_risk:.2f} ({'High Risk' if new_risk >= 0.6 else 'Medium Risk' if new_risk >= 0.35 else 'Low Risk'})")

st.subheader("Model Limitations")
st.markdown(
    """
- Rule based scoring may oversimplify complex student behaviors.
- Socio-economic features may introduce biases.
- Intended as a decision support tool, not a replacement for educators.
"""
)