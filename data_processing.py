'''Functions for processing scraped data'''

import sqlite3
from typing import List
import pandas as pd
from data import JOB_DB, JOB_COL

def write_to_dataframe(jobs: List[List[str]]) -> pd.DataFrame:
    '''Writes job data to dataframe'''
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame.from_records(jobs, columns=JOB_COL)
    return df

def write_to_csv(df: pd.DataFrame) -> None:
    '''Writes dataframe to csv'''
    df.to_csv(r'C:\Users\Joach\repos\job_finder\files\jobs.csv', encoding='utf-8')

def write_to_db(df: pd.DataFrame) -> None:
    '''Writes dataframe to database'''
    conn = sqlite3.connect(JOB_DB)
    df.to_sql('jobs', con=conn, if_exists='replace', index=False)
    conn.close()
