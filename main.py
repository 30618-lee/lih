import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

df = load_data()

# 데이터 미리보기
st.title("Google Drive 데이터 시각화")
st.write("데이터프레임 미리보기:")
st.dataframe(df)

# 컬럼 선택
columns = df.columns.tolist()
x_col = st.selectbox("X축 컬럼 선택", columns)
y_col = st.selectbox("Y축 컬럼 선택", columns, index=1)

# Plotly 시각화
fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
st.plotly_chart(fig)
