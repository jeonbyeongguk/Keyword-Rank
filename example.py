import streamlit as st
from pyppeteer import launch
import asyncio

# 페이지 기본 설정
st.set_page_config(page_title="My App", page_icon=":smiley:", layout="wide")

def main():
    st.title("테스트")
    st.write("Welcome to Streamlit!")
    st.write("This is a simple example.")

if __name__ == "__main__":
    main()

async def crawl_naver_pc(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(f'https://search.naver.com/search.naver?query={keyword}')
    
    # 원하는 내용을 가져오는 코드를 작성
    # 예를 들어, 페이지의 특정 요소를 선택하고 내용을 가져오는 등의 작업을 수행
    title1 = await page.evaluate(
        '''() => document.querySelector('#power_link_body > ul > li:nth-child(1) > div > div.title_url_area > a > span:nth-child(1)').textContent'''
    )
    title2 = await page.evaluate(
        '''() => document.querySelector('#power_link_body > ul > li:nth-child(2) > div > div.title_url_area > a > span:nth-child(1)').textContent'''
    )
    title3 = await page.evaluate(
        '''() => document.querySelector('#power_link_body > ul > li:nth-child(3) > div > div.title_url_area > a > span:nth-child(1)').textContent'''
    )
    
    # 페이지 내용을 가져온 후 반드시 브라우저를 닫아주어야 합니다.
    await browser.close()

    return title1, title2, title3

def search_keyword(keyword):
    loop = asyncio.get_event_loop()
    title1, title2, title3 = loop.run_until_complete(crawl_naver_pc(keyword))
    
    # 가져온 데이터를 출력합니다.
    st.write(title1)
    st.write(title2)
    st.write(title3)

input_keyword = st.text_input('검색할 키워드를 입력해주세요:', key='input_keyword')
if input_keyword:
    search_keyword(input_keyword)
