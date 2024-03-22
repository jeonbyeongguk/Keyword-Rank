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
        
        # HTML 응답 전체를 스트림릿 앱에서 확인할 수 있도록 출력합니다.
        # 주의: HTML 내용이 많을 수 있으므로, 실제 사용 시에는 주석 처리하는 것이 좋습니다.
        # st.text(html)  # 스트림릿 앱에서 직접 HTML 내용을 볼 수 있습니다.

        soup = BeautifulSoup(html, 'html.parser')
        title1 = soup.select_one('#power_link_body > ul > li:nth-child(1) > div > div.title_url_area > a > span:nth-child(1)')
        if title1:
            st.write(title1.get_text())
        else:
            st.write("첫 번째 검색 결과의 제목을 찾을 수 없습니다.")
    else:
        st.write(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()
