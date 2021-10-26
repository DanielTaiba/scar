import requests
from bs4 import BeautifulSoup

#selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options



def getSoup(url):
    try:
        page= requests.get(url)
        if page.status_code == 200:
           return BeautifulSoup(page.content, 'lxml')
    except Exception as e:
        print (f'Oops... {e}')
        return None
    

class chileAutos(object):
    def __init__(self) -> None:
        self.url='https://www.chileautos.cl/'
        self.categories=self.getCategories()
    
    def getCategories(self):
        mainPage=requests.get(self.url)

        if mainPage.status_code == 200:
            soup = BeautifulSoup(mainPage.content,'lxml')
            categories=soup.find_all(name='a',attrs={'class':'showroom-section-item'})
            endpoints=[]
            for cat in categories:
                endpoints.append(cat.get('href'))
            return endpoints
        else:
            return []
            

    def travelPages(self):
        url='https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/hatchback-categoria/?sort=lastupdated&offset='
        options=Options()
        options.page_load_strategy='eager'

        with webdriver.Firefox(options=options) as driver:
            for i in range(0,1000,12):
                driver.get(url+str(i))
                js = 'return document.documentElement.outerHTML'
                html = driver.execute_script(js)
                self.getCars(html)


    def getCars(self,html):
        soup=BeautifulSoup(html,'lxml')
        cars = soup.find_all(
            'div',
            attrs = {'class':'listing-item topspot','class':'listing-item showcase'}
            )
    
        for car in cars:
            #href
            ref=car.find_all('h3')
            print (ref[0].a['href'],'\n\n')
                    



