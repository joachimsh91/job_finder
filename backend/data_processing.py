'''Formats and stores scraped data'''

import sqlite3
from typing import List
import pandas as pd
from tabulate import tabulate
from backend.config import JOB_DB, JOB_COL

def write_to_dataframe(jobs: List[List[str]]) -> pd.DataFrame:
    '''Writes job data to dataframe'''
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame.from_records(jobs, columns=JOB_COL)
    print(tabulate(df.iloc[:, :-1], headers="keys", tablefmt="grid"))
    return df

def write_to_html(df: pd.DataFrame) -> None:
    '''Writes dataframe to HTML with hyperlinks'''
    df["Link"] = df["Link"].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
    df = df.style.set_table_styles([
        {'selector': 'th, td', 'props': [('text-align', 'left'), ('border', '1px solid black')]},
        {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%')]}
    ])
    df.to_html(r'C:\Users\Joach\repos\job_finder\backend\files\jobs.html', escape=False)

def write_to_csv(df: pd.DataFrame) -> None:
    '''Writes dataframe to csv'''
    df_copy = df.copy() 
    df_copy["Link"] = df_copy["Link"].str.extract(r'href="(.*?)"')
    df_copy.to_csv(r'C:\Users\Joach\repos\job_finder\backend\files\jobs.csv', index=False)

def write_to_db(df: pd.DataFrame) -> None:
    '''Writes dataframe to database'''
    conn = sqlite3.connect(JOB_DB)
    df_copy = df.copy() 
    df_copy["Link"] = df_copy["Link"].str.extract(r'href="(.*?)"')
    df_copy.to_sql('jobs', con=conn, if_exists='replace', index=False)
    conn.close()
