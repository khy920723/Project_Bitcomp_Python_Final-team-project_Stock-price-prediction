import crawler_financeCrawler


Crawler = crawler_financeCrawler.financeCrawler()
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
Crawler.crawler_setting('LG화학', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('KT&G', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('기아차', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('삼성전자', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('GS리테일', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('현대건설', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('CJ대한통운', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('KB금융', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('카카오', 2012, 1, 1, 2020, 11, 11)
Crawler.crawler_setting('비트컴퓨터', 2012, 1, 1, 2020, 11, 11)