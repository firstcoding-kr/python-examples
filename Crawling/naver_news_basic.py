import requests
from bs4 import BeautifulSoup
# 설치: 
# pip install requests
# pip install BeautifulSoup4

# 웹 페이지 요청
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
url = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103"
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.select_one('div.section_headline div.sh_text > a').text

print(text)
