"""
참고 링크: https://kkkapuq.tistory.com/63 얘는 안에 객체가 들어있는 형태
https://blog.naver.com/kiddwannabe/221274278923
https://m.blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221274285430&proxyReferer=https:%2F%2Fwww.google.com%2F
Maked by 형진

네이버 - 뉴스 - 속보 - 정치/경제/사회/생활&문화/세계/IT&과학/오피니언/연합뉴스속보 - 전체
생활문화 카테에서 1999년 기사까지 확인 가능

강사님 조언
css selector cheat sheet 검색(### cheat sheet 검색)
ex) https://www.pinterest.co.kr/pin/52002570677651321/

Beautifulsoup 사용 시 find는 숨겨진 태그들을 가져올 수도 있으므로 selector를 사용하는 것이 나음

"""
# -*- coding: utf-8, euc-kr -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import calendar
import crawler_parser
import os
import pandas as pd


class ArticleCrawler(object):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    def __init__(self):
        # 딕셔너리에서 value를 접근하려면 get()을 쓰거나 변수[키]로 접근해야 함
        self.sid1 = {'정치': 100, '경제': 101, '사회': 102, '생활/문화': 103, '세계': 104, 'IT/과학': 105}
        self.sid2 = {'청와대': 264, '국회/정당': 265, '북한': 268, '행정': 266, '국방/외교': 267, '정치일반': 269,
                     '금융': 259, '증권': 258, '산업/재계': 261, '중기/벤처': 771, '부동산': 260, '글로벌경제': 262, '생활경제': 310,
                     '경제일반': 263,
                     '사건사고': 249, '교육': 250, '노동': 251, '언론': 254, '환경': 252, '인권/복지': '59b', '식품/의료': 255, '지역': 256,
                     '인물': 276, '사회일반': 257,
                     '건강정보': 241, '자동차/시승기': 239, '도로/교통': 240, '여행/레저': 237, '음식/맛집': 238, '패션/뷰티': 376, '공연/전시': 242,
                     '책': 243, '종교': 244, '날씨': 248, '생활문화일반': 245,
                     '아시아/호주': 231, '미국/중남미': 232, '유럽': 233, '중동/아프리카': 234, '세계일반': 322,
                     '모바일': 731, '인터넷/SNS': 226, '통신/뉴미디어': 227, 'IT일반': 230, '보안/해킹': 732, '컴퓨터': 283, '게임/리뷰': 229,
                     '과학일반': 228,
                     }

    """
    # URL(카테고리&날짜&페이지): https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100&date=20201026&page=5
    # sid1&sid2&page: https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=268&date=20201026&page=3
    # URL(기사): https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=100&oid=469&aid=0000547909
    URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=' + str(sid1) + '&sid2=' + str(sid2)
    """

    def crawling_setting(self, input_sid1, start_year, start_month, end_year, end_month):

        if input_sid1 == '정치':
            # 청와대
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('청와대'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            print(sid1, sid2, article_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 국회/정당
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('국회/정당'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 북한
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('북한'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 행정
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('행정'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 국방/외교
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('국방/외교'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 정치일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('정치일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 국회/정당
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('국회/정당'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 북한
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('북한'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 행정
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('행정'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 국방/외교
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('국방/외교'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 정치일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('정치'), self.sid2.get('정치일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)

        elif input_sid1 == '경제':
            # 금융
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('금융'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 증권
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('증권'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 산업/재계
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('산업/재계'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 중기/벤처
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('중기/벤처'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 부동산
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('부동산'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 글로벌경제
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('글로벌경제'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 생활경제
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('생활경제'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 경제일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('경제'), self.sid2.get('경제일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)

        elif input_sid1 == '사회':
            # 사건사고
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('사건사고'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 교육
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('교육'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 노동
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('노동'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 언론
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('언론'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 환경
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('환경'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 인권/복지
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('인권/복지'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 식품/의료
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('식품/의료'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 지역
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('지역'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 인물
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('인물'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 사건사고
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('사건사고'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 교육
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('교육'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 노동
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('노동'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 언론
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('언론'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 환경
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('환경'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 인권/복지
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('인권/복지'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 식품/의료
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('식품/의료'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 지역
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('지역'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 인물
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('인물'), start_year, start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 사회일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('사회'), self.sid2.get('사회일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)

        elif input_sid1 == '생활/문화':
            # 건강정보
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('건강정보'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 자동차/시승기
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('자동차/시승기'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 도로/교통
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('도로/교통'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 여행/레저
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('여행/레저'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 음식/맛집
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('음식/맛집'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 패션/뷰티
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('패션/뷰티'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 공연/전시
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('공연/전시'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 책
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('책'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 종교
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('종교'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 날씨
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('날씨'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 생활문화일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('생활/문화'), self.sid2.get('생활문화일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)

        elif input_sid1 == '세계':
            # 아시아/호주
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('세계'), self.sid2.get('아시아/호주'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 미국/중남미
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('세계'), self.sid2.get('미국/중남미'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 유럽
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('세계'), self.sid2.get('유럽'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 중동/아프리카
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('세계'), self.sid2.get('중동/아프리카'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 세계일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('세계'), self.sid2.get('세계일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)

        elif input_sid1 == 'IT/과학':
            # 모바일
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('모바일'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 인터넷/SNS
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('인터넷/SNS'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 통신/뉴미디어
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('통신/뉴미디어'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # IT일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('IT일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 보안/해킹
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('보안/해킹'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 컴퓨터
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('컴퓨터'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 게임/리뷰
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('게임/리뷰'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)
            # 과학일반
            sid1, sid2, made_url_list = self.url_maker(self.sid1.get('IT/과학'), self.sid2.get('과학일반'), start_year,
                                                       start_month, end_year, end_month)
            sid1, sid2, article_list = self.crawling(sid1, sid2, made_url_list)
            self.toCSV(sid1, sid2, article_list, start_year, start_month, end_year, end_month)

    def url_maker(self, sid1, sid2, start_year, start_month, end_year, end_month):
        driver = webdriver.Chrome('D:\\chromedriver_win32\\chromedriver.exe')
        URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=' + str(sid1) + '&sid2=' + str(sid2)
        made_url_list = []
        driver.implicitly_wait(3)
        driver.get(URL)

        for year in range(start_year, end_year + 1):
            if start_year == end_year:
                year_startmonth = start_month
                year_endmonth = end_month
            else:
                if year == start_year:
                    year_startmonth = start_month
                    year_endmonth = 12
                elif year == end_year:
                    year_startmonth = 1
                    year_endmonth = end_month
                else:
                    year_startmonth = 1
                    year_endmonth = 12

            for month in range(year_startmonth, year_endmonth + 1):
                for month_day in range(1, calendar.monthrange(year, month)[1] + 1):
                    # for month_day in range(1, 3):  # 1일 부터 2일 까지 간단 테스트를 위한 코드
                    if len(str(month)) == 1:
                        month = "0" + str(month)
                    if len(str(month_day)) == 1:
                        month_day = "0" + str(month_day)

                    # 날짜별로 Page Url 생성
                    page_url = URL + '&date=' + str(year) + str(month) + str(month_day)

                    # 네이버 페이지 구조를 이용해서 page=999으로 지정해 해당 카테고리 뉴스의 총 페이지 수를 알아냄
                    # page=999을 입력할 경우 페이지가 존재하지 않기 때문에 page=totalpage로 이동 됨 (Redirect)
                    lastpage_url = page_url + "&page=999"
                    driver.get(lastpage_url)
                    html = driver.page_source
                    document_content = BeautifulSoup(html, 'html.parser')

                    lastpage_tag = document_content.select(".paging strong")[0]
                    # lastpage_tag = document_content.find('div', {'id': 'paging'})

                    for page in range(1, int(lastpage_tag.text) + 1):
                        made_url_list.append(page_url + "&page=" + str(page))

        print(sid1, sid2, made_url_list)
        return sid1, sid2, made_url_list

    def crawling(self, sid1, sid2, made_url_list):
        driver = webdriver.Chrome('D:\\chromedriver_win32\\chromedriver.exe')
        made_links = []  # 각 페이지별 url 이중리스트(요일별로 이중 리스트가 만들어짐)
        sum_made_links = []  # 이중리스트로 나온 made_links를 1차원 리스트로 만든 url 리스트
        article_list = []

        for urls in made_url_list:
            URL = urls
            driver.implicitly_wait(3)
            driver.get(URL)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            news_list = soup.select("div.list_body a")
            links = [tag['href'] for tag in news_list]
            links = set(links)
            # made_links가 이중 리스트 [{},{}] 형식으로 저장
            made_links.append(links)
        print(made_links)  # 성공 확인 완료

        # made_links를 1차원 리스트로 변경
        for i in made_links:
            sum_made_links += i
        print(sum_made_links)  # 성공 확인 완료

        # sum_made_links에서 각 링크를 받아와 date, title, content를 스크래핑 하는 부분
        for urls in sum_made_links:
            sleep(0.01)
            driver.get(urls)

            try:
                html_content = driver.page_source
                soup_content = BeautifulSoup(html_content, 'html.parser')
            except:
                continue

            try:
                title_tag = soup_content.find('h3', {'class': 'tts_head'})
                title = ''
                title = title + crawler_parser.ArticleParser.clear_headline(str(title_tag.text))

                write_date_tag = soup_content.find('span', {'class': 't11'})
                main_text_tag = soup_content.find('div', {'class': '_article_body_contents'})

                # 불필요한 태그 제거
                for main_text in soup_content.find_all('script'):
                    main_text.extract()

                main_text = ''
                main_text = main_text + crawler_parser.ArticleParser.clear_content(str(main_text_tag.text))

                for i in soup_content:  # soup_content가 True가 아닐 때(내용이 없을 때) 까지
                    temp = []  # 크롤링 한 뉴스 컬럼들을 날짜 순으로 1차원으로 뽑아내는 리스트
                    temp.append(write_date_tag.text)
                    temp.append(sid1)
                    temp.append(sid2)
                    temp.append(title)
                    temp.append(main_text)
                    temp.append(urls)
                    print(temp)
                article_list.append(temp)  # 1차원으로 뽑아낸 리스트를 2차원 리스트에 넣음
            except:
                continue

            print(article_list)  # 지금 스크래핑 하는 건 1차원에 뉴스 전체 컬럼들이 print 되면 됌

        return sid1, sid2, article_list

    def toCSV(self, sid1, sid2, article_list, start_year, start_month, end_year, end_month):
        # """
        # 참고링크 https://muzukphysics.tistory.com/292
        # """
        # # dataframe 행열 바꾸기
        input_sid1 = str(sid1)
        input_sid2 = str(sid2)
        data = pd.DataFrame()
        # data = pd.DataFrame(columns=['date', 'sid1', 'sid2', 'title', 'content', 'url'])

        for article in article_list:
            new_article = pd.DataFrame(article)
            # data.append(new_article.transpose(), ignore_index=True)
            data = pd.concat([data, new_article.transpose()], axis=0)

        print(data)
        data.columns = ['date', 'sid1', 'sid2', 'title', 'content', 'url']
        # data = pd.DataFrame(article_list)
        # data = pd.DataFrame(data, columns=['date', 'sid1', 'sid2', 'title', 'content', 'url'])
        # print(data.head())

        # \xa0, \xa9 를 없애줌
        data['content'] = data['content'].apply(
            lambda x: x.replace('\xa0', '').replace('\xa9', ''))  # column 하나가 = Series

        path_dir = f'D:\\Git\\주가예측_프로젝트\\-_-\\pyCharm\\naverNewsDB'
        path_dir_folder = os.path.join(path_dir, '{start_year}{start_month}_{end_year}{end_month}'.format(start_year=start_year,
                                                                                                          start_month=start_month,
                                                                                                          end_year=end_year,
                                                                                                          end_month=end_month))
        if not os.path.exists(path_dir_folder):
            os.makedirs(path_dir_folder)

        path_dir_csv = os.path.join(path_dir_folder, '{sid1}_{sid2}.csv'.format(sid1=input_sid1, sid2=input_sid2))
        data.to_csv(path_dir_csv, header=False, index=False)