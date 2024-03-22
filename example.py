import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import base64
import asyncio
from pyppeteer import launch

# 페이지 기본 설정
st.set_page_config(page_title="My App", page_icon=":smiley:", layout="wide")

def main():
    st.title("💡테스트")
    st.write("Welcome to Streamlit!")
    st.write("This is a simple example.")

if __name__ == "__main__":
    main()
    

def search_keyword(keyword):
    url = f'https://search.naver.com/search.naver?query={keyword}'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

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


def search_keyword_mo(keyword):
    url = f'https://m.search.naver.com/search.naver?query={keyword}'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title1 = soup.select_one('#power_link_body > li:nth-child(1) > div > div.tit_wrap > div > a > div.tit_area > span:nth-child(1) > mark')
        st.write(title1.get_text())
        
        title2 = soup.select_one('#power_link_body > li:nth-child(2) > div > div.tit_wrap > div > a > div.tit_area > span:nth-child(1) > mark')
        st.write(title2.get_text())
        
        title3 = soup.select_one('#power_link_body > li:nth-child(3) > div > div.tit_wrap > div > a > div.tit_area > span:nth-child(1) > mark')
        st.write(title3.get_text())

    else : 
        st.write(f"Error: {response.status_code}")


input_keyword_mo = st.text_input('검색할 키워드를 입력해주세요:', key='input_keyword_mo')
if input_keyword_mo:
    search_keyword_mo(input_keyword_mo)


async def crawl_naver_pc(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(f'https://search.naver.com/search.naver?query={keyword}')
    
    # 원하는 내용을 가져오는 코드를 작성
    # 예를 들어, 페이지의 특정 요소를 선택하고 내용을 가져오는 등의 작업을 수행
    
    # 페이지 내용을 가져온 후 반드시 브라우저를 닫아주어야 합니다.
    await browser.close()

input_keyword_crawl = st.text_input('검색할 키워드를 입력해주세요:', key='input_keyword_crawl')
if input_keyword_crawl:
    st.experimental_rerun()  # 이것으로 비동기적으로 코드를 다시 실행합니다.
