import streamlit as st
import requests
from bs4 import BeautifulSoup

# 페이지 기본 설정
st.set_page_config(page_title="My App", page_icon=":smiley:", layout="wide")

def main():
    st.title("💡테스트")
    st.write("Welcome to Streamlit!")
    st.write("This is a simple example.")

    input_keyword = st.text_input('검색할 키워드를 입력해주세요:', key='input_keyword')
    if input_keyword:
        search_keyword_debug(input_keyword)

def search_keyword_debug(keyword):
    url = f'https://search.naver.com/search.naver?query={keyword}'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract titles
        titles = soup.select('#power_link_body > ul > li > div > div.title_url_area > a > span:nth-child(1)')
        
        # Display titles
        for title in titles:
            st.write(title.get_text())

        
    
    else:
        st.write(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()
