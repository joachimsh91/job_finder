'''Contains lists of public and personal data used for scraper and mailer'''

URL_LINK = 'https://en.example.com&page=' # URL of website to scrape
JOB_DB = r'C:\Users\<username>\repos\job_finder\database\jobdata.sqlite' # Path/name of database
JOB_COL = ['Title', 'Company', 'Salary', 'Period', 'Location'] # Columns used for Pandas
MAIL_ADDRESS = ['sender_mail@gmail.com', 'reciever_mail@gmail.com'] # Sender and reciever mail address
MAIL_PASSWORD = ['<sender_mail app password'] # App password for sender email
TEMP_DATA = [] # Temporary storage of scraped data to be used for data processing
