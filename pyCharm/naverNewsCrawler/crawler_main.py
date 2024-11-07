"""
end 날짜를 주어주면 그 이상의 날짜를 선택했을 때 가장 최근 날짜의 뉴스가 나옴
"""
import crawler_articleCrawler

"""
self.sid1 = {'정치': 100, '경제': 101, '사회': 102, '생활/문화': 103, '세계': 104, 'IT/과학': 105}
"""
Crawler = crawler_articleCrawler.ArticleCrawler()
Crawler.crawling_setting('정치', 2020, 7, 2020, 7)
Crawler.crawling_setting('경제', 2020, 7, 2020, 7)
Crawler.crawling_setting('사회', 2020, 7, 2020, 7)
Crawler.crawling_setting('생활/문화', 2020, 7, 2020, 7)
Crawler.crawling_setting('세계', 2020, 7, 2020, 7)
Crawler.crawling_setting('IT/과학', 2020, 7, 2020, 7)