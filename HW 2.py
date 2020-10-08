# FE 595 HW 2 Minghao Kang
from requests_html import HTMLSession
import pandas as pd
import sys


def web_Scraper(url, times, file_Name):
    sel1 = 'body > ol > li'
    final_df = pd.DataFrame([])
    session = HTMLSession()
    try:
        for i in range(times):
            r = session.get(url)
            mylist = []
            results = r.html.find(sel1)
            for result in results:
                mytext = result.text
                mylist.append(mytext)
                mydf = pd.DataFrame(mylist)
            mydf.columns = ['text']
            Name = mydf[mydf['text'].str.contains('Name')]
            Purp = mydf[mydf['text'].str.contains('Purpose')]
            combin_df = pd.concat([Name.reset_index(drop=True), Purp.reset_index(drop=True)], axis=1)
            final_df = pd.concat([final_df, combin_df], ignore_index=True)
    except:
        sys.stderr.write('WARNING: CHECK YOUR URL')
        exit(2)
    final_df.columns = ['Name', 'Purpose']
    print(final_df)
    final_df.to_csv('./' + file_Name, index=False)


if __name__ == '__main__':
    url = 'http://3.95.249.159:8000/random_company'
    web_Scraper(url, 50, 'companies data.csv')
