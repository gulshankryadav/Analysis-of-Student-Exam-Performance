# save as app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("StudentsPerformance.csv")

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("📊 Student Exam Performance Dashboard")

# Filters
with st.sidebar:
    st.header("🔎 Filter Data")
    gender_filter = st.multiselect("Select Gender", df['gender'].unique(), default=df['gender'].unique())
    lunch_filter = st.multiselect("Select Lunch Type", df['lunch'].unique(), default=df['lunch'].unique())
    test_prep_filter = st.multiselect("Test Preparation", df['test preparation course'].unique(), default=df['test preparation course'].unique())

# Apply filters
filtered_df = df[
    (df['gender'].isin(gender_filter)) &
    (df['lunch'].isin(lunch_filter)) &
    (df['test preparation course'].isin(test_prep_filter))
]

# KPIs
st.subheader("📌 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("👥 Total Students", len(filtered_df))
col2.metric("📐 Avg Math Score", f"{filtered_df['math score'].mean():.2f}")
col3.metric("📖 Avg Reading Score", f"{filtered_df['reading score'].mean():.2f}")
col4.metric("✍️ Avg Writing Score", f"{filtered_df['writing score'].mean():.2f}")

st.divider()

# Gender-based average scores
st.subheader("📊 Gender-wise Average Scores")
gender_avg = filtered_df.groupby("gender")[['math score', 'reading score', 'writing score']].mean()
st.bar_chart(gender_avg)

# Lunch type impact
st.subheader("🍱 Lunch Type vs Scores")
lunch_avg = filtered_df.groupby("lunch")[['math score', 'reading score', 'writing score']].mean()
st.bar_chart(lunch_avg)

# Test preparation course impact
st.subheader("📘 Test Preparation vs Scores")
prep_avg = filtered_df.groupby("test preparation course")[['math score', 'reading score', 'writing score']].mean()
st.bar_chart(prep_avg)

# Parental education
st.subheader("🎓 Parental Education Level vs Performance")
edu_avg = filtered_df.groupby("parental level of education")[['math score', 'reading score', 'writing score']].mean()
fig1, ax1 = plt.subplots(figsize=(10, 4))
edu_avg.plot(kind='bar', ax=ax1)
plt.xticks(rotation=45)
plt.ylabel("Average Scores")
st.pyplot(fig1)

# Correlation heatmap
st.subheader("📈 Subject Score Correlation Heatmap")
fig2, ax2 = plt.subplots()
sns.heatmap(filtered_df[['math score', 'reading score', 'writing score']].corr(), annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

st.markdown("---")
st.caption("Dashboard by Gulshan 🔥")
