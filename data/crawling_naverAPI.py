import requests
import urllib
import json
import re
import csv

# API
client_id = '49JKBpbULBxHMj_VuN6u'
client_secret = 'l3FEO6r2pC'
header_params = {"X-Naver-Client-Id":client_id, 
                 "X-Naver-Client-Secret":client_secret}


input_list = ["김치", "반찬", "젓갈", "장류", "김", "튀각", "부각",\
              "과일", "견과류", "채소", "쌀", "잡곡","혼합곡", "건과류",\
              "쇠고기", "닭고기", "돼지고기","알류","축산가공식품","육류","양고기","오리고기",\
              "한방재료", "건강분말", "건강즙","과일즙", "꿀", "인삼", "홍삼", "건강환/정", "영양제", "비타민제", "환자식","영양보충식",\
              "통조림", "황도", "참치","연어", "골뱅이","번데기", "햄", "피클","올리브", "옥수수","콩", "꽁치","고등어",\
              "차류", "주스","과즙음료", "전통차","차음료", "건강음료","기능성음료", "우유","요구르트", "커피", "탄산음료", "코코아", "스무디", "두유","탄산수","제로음료",\
              "장아찌", "반찬류", "절임류", "조림류", "볶음류", "장조림",\
              "초콜릿", "떡", "스낵", "한과", "과자","쿠키","아이스크림","빙수", "가공안주류", "빵", "강정", "팝콘","강냉이류", "시리얼", "젤리", "전병", "엿", "푸딩", "사탕", "화과자", "베이커리","껌",\
              "건어물", "김","해초", "해산물","어패류", "생선", "수산가공식품", "젓갈","장류","조개류","게/갑각류","오징어","연체류","날치알","해삼","멍게",\
              "고추장", "양념장", "된장", "청국장", "쌈장", "간장", "장류", "매주",\
              "냉동식품","간편조리식품", "즉석국","즉석탕", "만두", "어묵", "튀김류", "누룽지", "즉석밥", "샐러드", "스프", "죽", "카레","짜장", "채식푸드", "떡볶이", "피자", "핫도그", "딤섬", "도시락", "햄버거",\
              "조미료", "고춧가루", "소금", "고추냉이", "식초", "물엿","올리고당", "겨자", "액젓", "설탕", "후추", "천연감미료",\
              "분말가루", "콩가루", "오트밀", "찹쌀가루", "쌀가루", "밀가루", "부침가루", "빵가루", "튀김가루",\
              "소스","드레싱","잼","시럽",\
              "치즈", "마가린", "버터", "생크림", "휘핑크림", "연유",\
              "콜라겐", "단백질보충제", "헬스보충제", "다이어트보조제", "곤약", "히알루론산", "식이섬유", "다이어트차", "다이어트식품",\
              "라면", "면류", "간식", "디저트", "구이", "밥","죽", "볶음", "튀김", "조림", "찜", "찌개", "국",\
              "샐러드", "닭가슴살", "만두", "딤섬", "햄버거", "맛살", "게살", "함박", "미트볼", "채식푸드",\
              "식용유", "오일","가루","분말류","향신료","제과재료","제빵재료",\
              "막걸리", "탁주", "약주", "소주", "일반증류주", "과실주", "리큐르주", "주류",\
              "비건", "동물복지", "지속가능수산", "무라벨음료"]


def crawl(query, header_params):
    start = 1
    for index in range(10):
        start_number = start + (index * 100)
        naver_shop_api = "https://openapi.naver.com/v1/search/shop?query=" + query + "&display=100&start=" + str(start_number)
        res = requests.get(naver_shop_api, headers=header_params)

        if res.status_code == 200:
            data = res.json()
            for item in data['items']:
                title = re.sub(cleanr, '', item['title']) # html 태그 제거
                price = item['lprice'] if item['lprice'] != 0 else item['hprice']
                cssWriter.writerow([title, item['category2'], item['category3'], price])
        else:
            print ("Error Code:", res.status_code)


# csv 파일 생성
f = open(r'naverAPI.csv', 'w',encoding= 'UTF-8') #mac
# r'C:\project\python\crawling2.csv', 'w',encoding= 'CP949', newline='' #window
cssWriter = csv.writer(f)
cssWriter.writerow(['title', 'category', 'sub_category', 'price']) # 컬럼
cleanr = re.compile('<.*?>') # 제거할 html 태그
# crawling
for search in input_list:
    query = urllib.parse.quote(search)
    crawl(query, header_params)

# 파일 닫기
f.close()

