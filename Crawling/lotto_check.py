import requests
from bs4 import BeautifulSoup

# 웹 페이지 요청
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
text = soup.select_one('.num > p').text

lotto = []

for span in soup.select('div.num.win > p span'):
    lotto.append(span.get_text(strip=True))

print(lotto)
