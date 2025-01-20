from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.chrome.service

driver = webdriver.Chrome()

page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

#fetch the webpage
driver.get(page_url)

#Wait for the table to load (adjustable)
driver.implicity_wait(10)

#Get the page source after JS execution
page_source = driver.page_source

#Parse the html content
soup = BeautifulSoup(page_source, 'html.parser')





