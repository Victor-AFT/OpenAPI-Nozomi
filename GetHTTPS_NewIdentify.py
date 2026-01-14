# date_creation: 22/12/2022
# date_modification: 07/02/2023
# Author: Victor Fuentes Toledo
# Version: 1.3


import requests
import urllib3

from datetime import datetime
from requests.auth import HTTPBasicAuth
import time
import csv


'MIRAR WHILE TRUE Y EL BREAK'
'Este script solicita las credenciales del usuario y ' \
'Lanza una peticion get a cada ip obteniendo el resultado de la query en un txt'

list_query_assets=[]
now =datetime.now()
time2 =now.strftime("%d-%m-%Y")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


myFileCSV=open('..\\Nozomi_assets_new.csv','w',encoding='utf-8', newline='')
writer=csv.writer(myFileCSV)



userr=input('introduce usuario: ')
pssword=getpass.getpass(prompt='Introduce credenciales: ')
#os.system("cls")
list_columnas=[]
data_rows=[]
def query_assets_cmc(ip):
    query_assets = 'query=assets | where days_ago(created_at) < 30'
    try:
        res_query_assets = requests.get('https://' + ip + '/api/open/query/do?' + query_assets,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_assets.raise_for_status()
        list_columnas = []
        for c in res_query_assets.json()['result']:

            for k,v in c.items():
                list_columnas.append(k)
            #print(list_columnas)
            writer.writerow(list_columnas)
            break
        for x in res_query_assets.json()['result']:
            data_rows = []
            for k,v in x.items():
                data_rows.append(v)
            #print(data_rows)
            writer.writerow(data_rows)


    except requests.exceptions.HTTPError:
        list_query_assets.append("0")
    except requests.exceptions.ConnectionError:
        #fa.write('%s %s - Connection Error\n' % (k, v))
        list_query_assets.append("0")



'Hay que crear un for general para que el resultado sea:'
'[IP,NOMBRE_SONDA,Q1,Q2,Q3,FECHA]'
'SI FALLA LA QUERY O NO HAY DATO SE PONE 0'
'FORMATO FECHA DD/MM/YEAR'
'CADA ARRAY ES LA SONDA Y ESCRIBIR EN UN FICHERO CSV CON RW SIEMPRE'
'LUEGO SI EXISTE SE REALIZA UN FTP'

#query_group(list_sondas)
#query_conteo(list_sondas)
#query_nodes(list_sondas)
#os.system('pause')

query_assets_cmc('10.0.0.1')
