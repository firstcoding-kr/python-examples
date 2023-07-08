# 네이버 뉴스 헤드라인 제목(멀티) 출력
import requests
from bs4 import BeautifulSoup

# 웹 페이지 요청
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# 방법1
for item in soup.select('.section_headline>.sh_list>li'):
    print(item.select_one('.sh_text_headline').get_text(strip=True))

# 방법2
for item in soup.select('.section_headline>.sh_list>li .sh_text_headline'):
    print(item.get_text(strip=True))
