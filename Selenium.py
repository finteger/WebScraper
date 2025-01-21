from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.chrome.service

driver = webdriver.Chrome()

page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

#fetch the webpage
driver.get(page_url)

#Wait for the table to load (adjustable)
driver.implicitly_wait(10)

#Get the page source after JS execution
page_source = driver.page_source

#Parse the html content
soup = BeautifulSoup(page_source, 'html.parser')

#Find the table element
table = soup.find('table', class_='pub-table')


if table:
    #Extract column headers
    headers = [th.get_text().strip() for th in table.find_all('th')]
    
    #Extract the row data
    rows = []
    for tr in table.find_all('tr'):
        row = [td.get_text().strip() for td in tr.find_all('td')]
        if row:
            rows.append(row)
            
    print('Column headers:')    
    print(headers)  
    
    print('\nRow data:')
    for row in rows:
        print(row)    
        
    header_type = (
      'All-items',
      'Food',
      'Shelter',
      'Householder operations, furnishings, equipment',
      'Clothing & footwear',
      'Transportation',
      'Gasoline',
      'Health & Personal Care',
      'Recreation, education & reading',
      'Alcoholic beverages, tobacco products & recreational cannabis',
      'All-items excluding food & energy',
      'All-items excluding energy',
      'Energy',
      'Goods',
      'Services', 
    )
        
    
 
            
        





