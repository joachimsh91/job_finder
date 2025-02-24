'''Main module'''

from mailer import send_mail
from scraper import scrape_pages
from data import TEMP_DATA
from data_processing import write_to_dataframe, write_to_csv, write_to_db

def main():
    '''Main function'''
    scrape_pages(1, 4)
    job_data = write_to_dataframe(TEMP_DATA)
    print(job_data)
    write_to_csv(job_data)
    write_to_db(job_data)
    prompt = input('Send job listings to email? (y/n) ')
    if prompt == 'y':
        send_mail()
    elif prompt == 'n':
        pass

if __name__ == '__main__':
    main()
