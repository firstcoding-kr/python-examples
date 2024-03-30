# 모듈 설치 (cmd창): pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

dv = webdriver.Chrome()

# 네이버로 이동한다.
dv.get('https://www.naver.com')
time.sleep(1)

# 검색창을 찾는다
search = dv.find_element(By.ID, 'query')
search.send_keys('진주 코딩학원', Keys.ENTER)
time.sleep(1)

# 퍼스트코딩을 찾는다.
fc = dv.find_element(By.CSS_SELECTOR, '#loc-main-section-root > section > div > div.rdX0R.HXTER > ul > li:nth-child(4) > div.qbGlu > div.ouxiq > a:nth-child(1) > div > div > span.YwYLL')

# 해당 위치로 스크롤 이동
actions = ActionChains(dv)
actions.move_to_element(fc).perform()
fc.click()

# 탭이 열린다. - 잠시 기다림 
time.sleep(2)

# 새로 열린 탭으로 포커스 이동
tabs = dv.window_handles
print('탭정보: ', tabs)
dv.switch_to.window(tabs[-1])

# iframe (웹페이지 내에 또다른 웹페이지) 전환
iframe = dv.find_element(By.ID, 'entryIframe')
dv.switch_to.frame(iframe)

# 주소정보 찾기
주소정보 = dv.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div:nth-child(5) > div > div:nth-child(2) > div.place_section_content > div > div.O8qbU.tQY7D > div')
주소정보 = 주소정보.text

#주소 출력
print('퍼스트코딩주소: ', 주소정보)

time.sleep(3)
