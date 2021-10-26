#selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#beautiful soup
from bs4 import BeautifulSoup


options=Options()
options.page_load_strategy='eager'

driver = webdriver.Firefox(options=options)
url = 'https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/hatchback-categoria/?sort=lastupdated&offset='
driver.get(url)
#js = 'return document.documentElement.outerHTML'
#html = driver.execute_script(js)
next_page=driver.find_element_by_class_name('page-link next ')
next_page.click()
#soup = BeautifulSoup(html,'lxml')

#print (soup.prettify())

driver.quit()
#with open('index.html','w') as f:
#   f.write(html)
