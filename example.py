import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # 웹사이트에 GET 요청 보내기
    response = requests.get(url, headers=headers)
    
    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # HTML 파싱
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # 원하는 데이터 추출
        titles = soup.select('.title')  # 예시: CSS 선택자를 사용하여 타이틀을 추출
        
        for title in titles:
            print(title.text)  # 타이틀 출력 또는 다른 처리 수행
    else:
        print(f"Error: {response.status_code}")

# 크롤링할 웹사이트 URL
url = 'https://example.com'
crawl_website(url)
