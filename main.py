import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 로드
@st.cache_data
def load_data():
    return pd.read_csv("diabetes_data.csv")

st.title("당뇨병 데이터 시각화")
df = load_data()

st.write("데이터 미리보기:")
st.dataframe(df.head())

# class 기준 그룹 평균
symptom_columns = df.columns[:-1]  # 'class' 제외
class_grouped = df.groupby('class')[symptom_columns].mean().T
class_grouped.columns = ['No Diabetes', 'Diabetes']
class_grouped = class_grouped.reset_index().rename(columns={'index': 'Symptom'})

# 시각화
fig = px.bar(
    class_grouped,
    x='Symptom',
    y=['No Diabetes', 'Diabetes'],
    barmode='group',
    title='당뇨병 유무에 따른 증상 발생 평균 비교',
    labels={'value': '증상 발생 평균'}
)
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)
