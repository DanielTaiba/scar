import pandas as pd
import csv
import os


class dfCars():
    def __init__(self) -> None:
        self.columns=['Nombre','Type','Href','Vendedor','Location','Precio','Kms','Transmision','Tipo_combustible','Consumo']
        self.fileName='./dataCars.csv'
    

    def createCSV(self):
        with open(self.fileName,'w',encoding='UTF8') as f:
            writer=csv.writer(f)
            writer.writerow(self.columns)

    def saveCar(self,dataCar={}):

        if not os.path.isfile(self.fileName):
            self.createCSV()

        with open(self.fileName,'a',encoding='UTF8', newline='') as f:
            #datos
            row=[
                dataCar['Nombre'],
                dataCar['Type'],
                dataCar['Href'],
                dataCar['Vendedor'],
                dataCar['Location'],
                dataCar['Precio'],
                dataCar['Kms'],
                dataCar['Nombre'],
                dataCar['Transmision'],
                dataCar['Tipo_combustible'],
                dataCar['Consumo'],
            ]
            #escribir csv
            writer=csv.writer(f)
            writer.writerow(row)

        
           