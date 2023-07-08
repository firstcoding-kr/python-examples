# 유튜브 검색결과 10건을 Youtube Data API를 이용하여 가져온다.
import requests, json

api_key = "" # api key 발급 필요함
max_result = 10

keyword = input('검색어를 입력해주세요: ')

# 웹 API 요청
url = f"https://www.googleapis.com/youtube/v3/search?part=id,snippet&q={keyword}&maxResults={max_result}&key={api_key}"
response = requests.get(url)

# 결과를 json 형태로 가져온다.
json_dict = response.json() # 딕셔너리 형태로 가져오기
json_str = json.dumps(json_dict, indent=2, ensure_ascii=False) # 문자열로 가져오기

# json 문자열 출력해보기
print(json_str)

# json 파일로 저장
with open('youtube_search.json', 'w', encoding="utf8") as f:
    f.write(str(json_str))

# 제목만 뽑아서 출력해보기
for item in json_dict['items']:
    print(item['snippet']['title'])
