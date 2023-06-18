import os
import glob
import pandas as pd
os.chdir("C:\\Temp\\uoc\\Visualización de datos\\Practica 2\\Conjunto_datos_origen\\OK")

extension = 'csv'
todos_los_archivos = [i for i in glob.glob('*.{}'.format(extension))]

#combina todos los archivos de la lista
combinado_csv = pd.concat([pd.read_csv(f) for f in todos_los_archivos ])


#exporta a csv
combinado_csv.to_csv( "Todo_Junto.csv", index=False, encoding='utf-8-sig')
