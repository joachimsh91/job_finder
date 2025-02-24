# job_finder
Web scraper written in Python for finding job listings.
Currently in development as a portfolio project.

How to use:

1. Find a job listing website, make a search and save the base URL e.g. https://www.example.com/job/fulltime/search.html?page=
2. In your url, the number after "page=" is the page number. Check how many pages the search result has, and take note of start and end page number
3. Go to data.py. This is where your public and personal data to be used by the web scraper and mailer will be stored
4. Paste your base URL into URL_LINK in data.py
5. Fill in the path and name of the database in JOB_DB
6. Fill in sender and reciever email address in MAIL_ADDRESS
7. Fill in sender email app password in MAIL_PASSWORD
8. Let ALL_DATA stay empty, this is the temporary storage for scraped data
9. The web scraper is run from main.py. Insert the number of first page and end page in scrape_pages() before running the script

NOTE: Currently the scraper functions has hardcoded html tags from the website I used to scrape data. As of now these html tags needs to be changed depending on what 
site you plan to scrape.

TO BE UPDATED
