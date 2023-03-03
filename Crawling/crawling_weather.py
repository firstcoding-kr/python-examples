import requests
from bs4 import BeautifulSoup

# 지역 입력
region = input("지역을 입력하세요: ")

# 날씨 페이지 요청
url = f"https://search.naver.com/search.naver?query={region}+날씨"
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 현재 온도, 날씨 상태 추출
temp = soup.select_one('div.temperature_text').text
weather = soup.select_one('span.weather').text

# 미세먼지, 초미세먼지 추출
dust = soup.select_one('li.level1 .txt').text
fine_dust = soup.select_one('li.level1 .txt').text

# 결과 출력
print(f"현재 {region} 날씨")
print(f"온도: {temp}")
print(f"상태: {weather}")
print(f"미세먼지: {dust}")
print(f"초미세먼지: {fine_dust}")
