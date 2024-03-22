import streamlit as st
import requests
from bs4 import BeautifulSoup

def search_keyword(keyword):
    url = f'https://search.naver.com/search.naver?query={keyword}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        titles = []
        for i in range(1, 4):
            title = soup.select_one(f'#power_link_body > ul > li:nth-child({i}) > div > div.title_url_area > a > span:nth-child(1)')
            if title:
                titles.append(title.get_text())
        
        if titles:
            for title in titles:
                st.write(title)
        else:
            st.write("No titles found.")
    else:
        st.write(f"Error: {response.status_code}")

def main():
    st.title("Web Page Title Scraper")
    st.write("Enter a keyword to search for:")
    keyword = st.text_input("Keyword")
    
    if st.button("Search"):
        if keyword:
            search_keyword(keyword)
        else:
            st.write("Please enter a keyword.")

if __name__ == "__main__":
    main()
