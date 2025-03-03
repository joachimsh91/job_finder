'''Functions for job hunting'''

from typing import List
import requests
from bs4 import BeautifulSoup
from backend.config import URL_LINK, TEMP_DATA

def get_page(url: str, page: int) -> str:
    '''Connects to page'''
    response = requests.get(url + str(page), timeout=10)
    return response

def page_parser(response: str) -> BeautifulSoup:
    '''Parses page content'''
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_titles(soup: BeautifulSoup) -> List[str]:
    '''Gets job titles'''
    return [title.get_text(strip=True) for title in soup.find_all('h3', class_='list_h3')]

def get_companies(soup: BeautifulSoup) -> List[str]:
    '''Gets companies'''
    companies = soup.find_all('span', class_='heading_secondary')
    return [(company.find('span', class_='dib mt5 mr5').get_text(strip=True)
            if company.find('span', class_='dib mt5 mr5') else "N/A")
            for company in companies]

def get_salaries(soup: BeautifulSoup) -> List[str]:
    '''Gets salaries'''
    salaries = soup.find_all('div', class_='jobadlist_list_cell_salary')
    return [(salary.find('span', class_='salary_amount').get_text(strip=True)
            if salary.find('span', class_='salary_amount') else "N/A")
            for salary in salaries]

def get_periods(soup: BeautifulSoup) -> List[str]:
    '''Gets salary periods'''
    periods = soup.find_all('div', class_='jobadlist_list_cell_salary')
    return [(period.find('span', class_='salary_period').get_text(strip=True)
            if period.find('span', class_='salary_period') else "N/A")
            for period in periods]

def get_locations(soup: BeautifulSoup) -> List[str]:
    '''Gets job locations'''
    locations = soup.find_all('span', class_='txt_list_1')
    return [(location.find('span', class_='list_city').get_text(strip=True)
            if location.find('span', class_='list_city') else "N/A")
            for location in locations]

def get_links(soup: BeautifulSoup) -> List[str]:
    '''Gets link to job post'''
    links = soup.find_all('a', class_='list_a can_visited list_a_has_logo')
    return [(link.get('href')
            if link.get('href') else "N/A")
            for link in links]

def get_jobs(soup: BeautifulSoup) -> List[List[str]]:
    '''Collects job data from parsed page content'''
    job_data = []
    titles = get_titles(soup)
    companies = get_companies(soup)
    salaries = get_salaries(soup)
    periods = get_periods(soup)
    locations = get_locations(soup)
    links = get_links(soup)

    for i in range(max(len(titles), len(companies), len(salaries),
                       len(periods), len(locations), len(links))):
        title = titles[i] if i < len(titles) else "N/A"
        company = companies[i] if i < len(companies) else "N/A"
        salary = salaries[i] if i < len(salaries) else "N/A"
        period = periods[i] if i < len(periods) else "N/A"
        location = locations[i] if i < len(locations) else "N/A"
        link = links[i] if i < len(links) else "N/A"
        job_data.append([title, company, salary, period, location, link])

    return job_data

def scrape_pages(first_page: int, end_page: int):
    '''Scrapes data for selected pages and stores data in list'''
    for page in range(first_page, end_page):
        request = get_page(URL_LINK, page)
        soup = page_parser(request)
        data = get_jobs(soup)
        TEMP_DATA.extend(data)
