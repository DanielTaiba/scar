#selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import os 
from data import dfCars
from bs4 import BeautifulSoup


class chileAutos (object):
	def travelPages(self):
		url='https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/hatchback-categoria/?sort=lastupdated&offset='
		options=Options()
		options.page_load_strategy='eager'

		with webdriver.Firefox(options=options) as driver:
			for i in range(0,1000,12):
				driver.get(url+str(i))
				js = 'return document.documentElement.outerHTML'
				html = driver.execute_script(js)
				#self.getCars(html)
				with open(f'./html/pages/page_{str(i/12+1)}.html','w') as f:
					f.write(html)

	def getCars(self):
		base_dir='./html/pages/'
		for page in os.listdir(base_dir):
			with open(base_dir+page,'r') as html:
				soup = BeautifulSoup(html,'lxml')
				cars = soup.find_all(
					'div',
					attrs = {'class':'listing-item topspot','class':'listing-item showcase'}
					)

				for car in cars:
					data=dfCars().newCar()
					#nombre
					try:
						data['Nombre']=car.find_all('h3')[0].a.string
					except:
						data['Nombre']=None
					#type
					try:
						data['Type']='Hatchback'
					except:
						data['Type']=None

					#href vehiculo
					try:
						data['Href']=car.find_all('h3')[0].a['href']
					except:
						data['Href']=None
					#seller-type
					try:
						data['Vendedor']=car.find_all('span',attrs={'class':'seller-type'})[0].string
					except:
						data['Vendedor']=None
					#location
					try:
						data['Location']=car.find_all('span',attrs={'class':'seller-location'})[0].string
					except:
						data['Location']=None
					#price
					try:
						data['Precio']=car.find_all('div',attrs={'class':'price'})[0].a.string
					except:
						data['Precio']=None

					#car details
					ref=car.find_all('div',attrs={'class':'key-detail'})
					for r in ref:
						try:
							t=r.contents[1].string
							v=r.contents[3].string
							if t=='Kilometraje ':
									data['Kms']=v
							elif t=='Transmisión ':
									data['Transmision']=v
							elif t=='Combustible ':
									data['Tipo_combustible']=v
							elif t=='Consumo mixto':
									data['Consumo']==v
						except:
							pass
					
					dfCars().saveCar(dataCar=data)

