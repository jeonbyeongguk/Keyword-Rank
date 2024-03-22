import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import base64

# 페이지 기본 설정
st.set_page_config(page_title="My App", page_icon=":smiley:", layout="wide")

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



def search_keyword(keyword):
    url = f'https://search.naver.com/search.naver?query={keyword}'
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title1 = soup.select_one('#power_link_body > ul > li:nth-child(1) > div > div.title_url_area > a > span:nth-child(1)')
        st.write(title1.get_text())
        
        title2 = soup.select_one('#power_link_body > ul > li:nth-child(2) > div > div.title_url_area > a > span:nth-child(1)')
        st.write(title2.get_text())
        
        title3 = soup.select_one('#power_link_body > ul > li:nth-child(3) > div > div.title_url_area > a > span:nth-child(1)')
        st.write(title3.get_text())

    else : 
        st.write(f"Error: {response.status_code}")


input_keyword = st.text_input('검색할 키워드를 입력해주세요:', key='input_keyword')
if input_keyword:
    search_keyword(input_keyword)



# 중앙에 위치하고 크기를 키우기 위해 HTML 사용
st.markdown('<h1 style="text-align:center;">Countdown</h1>', unsafe_allow_html=True)
ph = st.empty()
N = 5*60
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    # 크기를 조절하고 가운데 정렬
    ph.markdown(f'<h2 style="text-align:center;">{mm:02d}:{ss:02d}</h2>', unsafe_allow_html=True)
    time.sleep(1)
