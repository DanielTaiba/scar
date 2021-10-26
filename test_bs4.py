from bs4 import BeautifulSoup
from data import dfCars

data={
            'Nombre':None,
            'Type':None,
            'Href':None,
            'Vendedor':None,
            'Location':None,
            'Precio':None,
            'Kms':None,
            'Transmision':None,
            'Tipo_combustible':None,
            'Consumo':None,
        }


with open('html/index.html','r') as html:
    soup = BeautifulSoup(html,'lxml')
    cars = soup.find_all(
        'div',
        attrs = {'class':'listing-item topspot','class':'listing-item showcase'}
        )

    for car in cars:
        data={}
        #ref=car.find_all('h3')
        #nombre vehiculo
        #print (ref[0].a.string)
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
        #print (car.find_all('h3')[0].a['href'])
        try:
            data['Href']=car.find_all('h3')[0].a['href']
        except:
            data['Href']=None
        #seller-type
        #print(car.find_all('span',attrs={'class':'seller-type'})[0].string)
        try:
            data['Vendedor']=car.find_all('span',attrs={'class':'seller-type'})[0].string
        except:
            data['Vendedor']=None
        #location
        #print(car.find_all('span',attrs={'class':'seller-location'})[0].string)
        try:
            data['Location']=car.find_all('span',attrs={'class':'seller-location'})[0].string
        except:
            data['Location']=None
        #price
        #print(car.find_all('div',attrs={'class':'price'})[0].a.string)
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
                print(f'{t}:{v}')
                if t=='Kilometraje ':
                    data['Kms']=v
                elif t=='Transmisión ':
                    data['Transmision']=v
                elif t=='Combustible ':
                    data['Tipo_combustible']=v
                elif t=='Consumo mixto ':
                    data['Consumo']==v
            except:
                pass
        
        dfCars().saveCar(dataCar=data)
        
        #print('')
        

    #print (len(cars))
    
    """
    with open('cars.html','w') as f:
        f.write(cars[0].prettify())
    """