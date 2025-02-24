'''Scrapes pages from web site'''

from data import URL_LINK, TEMP_DATA
from scraper_functions import get_page, page_parser, get_jobs

def scrape_pages(first_page: int, end_page: int):
    '''Scrapes data for selected pages and stores data in list'''
    for page in range(first_page, end_page):
        request = get_page(URL_LINK, page)
        soup = page_parser(request)
        data = get_jobs(soup)
        TEMP_DATA.extend(data)
