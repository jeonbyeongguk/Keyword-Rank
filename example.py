import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import base64

# 페이지 기본 설정
st.set_page_config(
    page_icon="💡",
    page_title="테스트",
    layout="wide",
)
def main():
    st.title("💡테스트")
    st.write("Welcome to Streamlit!")
    st.write("This is a simple example.")

if __name__ == "__main__":
    main()
    

uploaded_file = st.file_uploader("'CSV' 또는 'xlsx' 파일 업로드하세요!!", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # 업로드된 파일을 데이터프레임으로 읽기
        if uploaded_file.name.endswith('csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('xls', 'xlsx')):
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        else:
            st.error('올바른 파일 형식이 아닙니다. CSV 또는 엑셀 파일을 업로드해주세요.')
            st.stop()

        # 데이터프레임 표시
        st.write(df)
    except Exception as e:
        st.error(f'오류 발생: {e}')

keyword = "영어문제"

url = f'https://m.search.naver.com/search.naver?query={keyword}'

response = requests.get(url)

st.write("요청에 사용된 헤더:")
st.write(response.request.headers)
