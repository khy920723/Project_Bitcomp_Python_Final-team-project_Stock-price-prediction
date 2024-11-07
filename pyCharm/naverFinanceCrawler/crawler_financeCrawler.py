"""
참고 링크: http://blog.quantylab.com/crawling_naverfin_daycandle.html 네이버 금융에서 주식 종목의 일별 주가 크롤링하기
"""
from bs4 import BeautifulSoup
import requests
import traceback
import pandas as pd
import datetime
import os

class financeCrawler:

    def __init__(self):
        """
        테마 - 종목
        화학 - LG화학 / 2001.04.25
        음식료 - KT&G / 1999.10.08
        운수장비 - 기아차 / 1996.06.25
        전기/전자 - 삼성전자 / 1996.06.25
        유통 - GS리테일 / 2011.12.23
        건설 - 현대건설 / 1996.06.25
        운수창고 - CJ대한통운 / 1996.06.25
        금융 - KB금융 / 2008.10.10
        서비스 - 카카오 / 1999.11.11
        의료 - 비트컴퓨터 / 1998.05.09
        """
        self.stuff = {"LG화학": "051910",
                      "KT&G": "033780",
                      "기아차": "000270",
                      "삼성전자": "005930",
                      "GS리테일": "007070",
                      "현대건설": "000720",
                      "CJ대한통운": "000120",
                      "KB금융": "105560",
                      "카카오": "035720",
                      "비트컴퓨터": "032850"}


    def crawler_setting(self, stuff, start_year, start_month, start_day, end_year, end_month, end_day):
        str_datefrom = datetime.datetime.strftime(datetime.datetime(year=start_year, month=start_month, day=start_day), '%Y.%m.%d')
        print(str_datefrom)
        str_dateto = datetime.datetime.strftime(datetime.datetime(year=end_year, month=end_month, day=end_day), '%Y.%m.%d')
        print(str_dateto)

        code, pg_last = self.make_lastpg(stuff)
        df = None

        for page in range(1, pg_last + 1):
            _df = self.parse_page(code, page)
            _df_filtered = _df[_df['날짜'] > str_datefrom]
            if df is None:
                df = _df_filtered
            else:
                df = pd.concat([df, _df_filtered])
            if len(_df) > len(_df_filtered):
                break
        print(df)

        df['code'] = code

        self.toCSV(code, str_datefrom, str_dateto, df)


    def make_lastpg(self, stuff):
        code = self.stuff.get(stuff)

        url = "https://finance.naver.com/item/sise_day.nhn?code=" + code
        res = requests.get(url)
        res.encoding = 'utf-8'
        print(res.status_code)
        print(url)


        soap = BeautifulSoup(res.text, 'lxml')
        """
        Pagination 영역을 가져와서 마지막 페이지 번호를 알아냄
        테이블 아래 부분에 Pagination 영역이 있는데 이 또한 <table>로 구성되어 있음
        """
        el_table_navi = soap.find("table", class_="Nnavi")
        el_td_last = el_table_navi.find("td", class_="pgRR")
        pg_last = el_td_last.a.get('href').rsplit('&')[1]
        pg_last = pg_last.split('=')[1]
        pg_last = int(pg_last)
        print(pg_last) # 마지막 페이지 확인

        """
        마지막 페이지 번호 내에서 원하는 페이지의 테이블을 읽을 수 있음
        parse_page(): 종목과 페이지 번호를 입력 받아 일별 주가를 Pandas DataFrame객체로 반환
        """
        return code, pg_last

    def parse_page(self, code, page):
        try:
            url = 'http://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'.format(code=code, page=page)
            res = requests.get(url)
            _soap = BeautifulSoup(res.text, 'lxml')
            _df = pd.read_html(str(_soap.find("table")), header=0)[0]
            _df = _df.dropna()
            return _df
        except Exception as e:
            traceback.print_exc()
        return None

        print(parse_page(code, 1))


    def toCSV(self, code, str_datefrom, str_dateto, df):

        path_dir = 'D:\\Git\\주가예측_프로젝트\\-_-\\pyCharm\\naverFinanceCrawler\\2020-11-11'
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        path = os.path.join(path_dir, '{code}_{date_from}_{date_to}.csv'.format(code=code, date_from=str_datefrom,
                                                                                date_to=str_dateto))
        print(path)

        df.to_csv(path, header=False, index=False)
