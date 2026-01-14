# date_creation: 22/12/2022
# Author: Victor Fuentes Toledo
# Version: 1.4

import paramiko
import requests
import urllib3
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os
import time
import csv


list_query_assets=[]
now =datetime.now()
time2 =now.strftime("%d-%m-%Y")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
list_sondas={'192.168.1.5':'AA','192.168.1.6':'BB'}
cadena_error='ErrorLectura'


'CONEXION SSH ELK'
hostname='192.168.1.2'
port=22


'USUARIO ELK'
username='userelk'
password='12345'
'Nozomi_nodos_enlaces'
path_file_local='Output/Nozomi_opensearch.csv'
path_file_remote='/opt/kpi-nozomi-logstash/Nozomi_opensearch.csv'


myFileCSV=open(path_file_local,'w',encoding='utf-8', newline='')
writer=csv.writer(myFileCSV)

'USUARIO NOZOMI'
userr='nozomi'
pssword='nozomi'


def query_conteo(k,v):
    query_conteo = 'query=alerts | where hours_ago(time) < 24 | sort time | select id type_id appliance_host time'
    try:
        res_query_conteo = requests.get('https://' + k + '/api/open/query/do?' + query_conteo,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_conteo.raise_for_status()
        if res_query_conteo.status_code==200:
                file_bruto_query_conteo = res_query_conteo.text
                texto_bruto_conteo = file_bruto_query_conteo.split(",")
                if texto_bruto_conteo[-1] == '{"result":null':
                    list_query_assets.append(k)
                    list_query_assets.append(v)
                    list_query_assets.append('0')
                else:
                    clear_texto_bruto_conteo = texto_bruto_conteo[-1].replace('"total":', '')
                    clear_caracter_bruto_conteo = clear_texto_bruto_conteo.replace('}', '')
                    list_query_assets.append(k)
                    list_query_assets.append(v)
                    list_query_assets.append(clear_caracter_bruto_conteo)
    except requests.exceptions.HTTPError:
        try:
            res_query_conteo_while_3 = requests.get('https://' + k + '/api/open/query/do?' + query_conteo,auth=HTTPBasicAuth(userr, pssword), verify=False)
            res_query_conteo_while_3.raise_for_status()
            if res_query_conteo_while_3.status_code == 200:
                file_bruto_query_conteo_3 = res_query_conteo_while_3.text
                texto_bruto_3 = file_bruto_query_conteo_3.split(",")
                if texto_bruto_3[-1] == '{"result":null':
                    list_query_assets.append(k)
                    list_query_assets.append(v)
                    list_query_assets.append('0')
                else:
                    clear_texto_bruto_conteo_3 = texto_bruto_3[-1].replace('"total":', '')
                    clear_caracter_bruto_conteo_3 = clear_texto_bruto_conteo_3.replace('}', '')
                    list_query_assets.append(k)
                    list_query_assets.append(v)
                    list_query_assets.append(clear_caracter_bruto_conteo_3)
        except requests.exceptions.HTTPError:
            list_query_assets.append(k)
            list_query_assets.append(v)
            list_query_assets.append(cadena_error)
        except requests.exceptions.ConnectionError:
            list_query_assets.append(k)
            list_query_assets.append(v)
            list_query_assets.append(cadena_error)
    except requests.exceptions.ConnectionError:
        list_query_assets.append(k)
        list_query_assets.append(v)
        list_query_assets.append(cadena_error)
    time.sleep(1)
    return list_query_assets

def query_nodes(k,v):
    query_nodes = 'query=nodes | where days_ago(created_at) < 1'
    try:
        res_query_nodes = requests.get('https://' + k + '/api/open/query/do?' + query_nodes,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_nodes.raise_for_status()
        if res_query_nodes.status_code==200:
            file_bruto_query_nodes = res_query_nodes.text
            texto_bruto = file_bruto_query_nodes.split(",")
            if texto_bruto[-1] == '{"result":null':
                list_query_assets.append('0')
            else:
                clear_texto_bruto=texto_bruto[-1].replace('"total":','')
                clear_caracter_bruto=clear_texto_bruto.replace('}','')
                list_query_assets.append(clear_caracter_bruto)
    except requests.exceptions.HTTPError:
        try:
            res_query_nodes_3 = requests.get('https://' + k + '/api/open/query/do?' + query_nodes,auth=HTTPBasicAuth(userr, pssword), verify=False)
            res_query_nodes_3.raise_for_status()
            if res_query_nodes_3.status_code == 200:
                    file_bruto_query_nodes_3 = res_query_nodes_3.text
                    texto_bruto_3 = file_bruto_query_nodes_3.split(",")
                    if texto_bruto_3[-1] == '{"result":null':
                        list_query_assets.append('0')
                    else:
                        clear_texto_bruto = texto_bruto_3[-1].replace('"total":', '')
                        clear_caracter_bruto = clear_texto_bruto.replace('}', '')
                        list_query_assets.append(clear_caracter_bruto)
        except requests.exceptions.HTTPError:
            list_query_assets.append(cadena_error)
        except requests.exceptions.ConnectionError:
            list_query_assets.append(cadena_error)
    except requests.exceptions.ConnectionError:
        list_query_assets.append(cadena_error)
    time.sleep(1)
    return list_query_assets

def query_assets(k,v):
    query_assets = 'query=assets | where days_ago(created_at) < 1'
    try:
        res_query_assets = requests.get('https://' + k + '/api/open/query/do?' + query_assets,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_assets.raise_for_status()
        if res_query_assets.status_code == 200:
                file_bruto_query_assets = res_query_assets.text
                texto_bruto_assets = file_bruto_query_assets.split(",")
                if texto_bruto_assets[-1] == '{"result":null':
                    list_query_assets.append('0')
                else:
                    clear_texto_bruto_assets = texto_bruto_assets[-1].replace('"total":', '')
                    clear_caracter_bruto_assets = clear_texto_bruto_assets.replace('}', '')
                    list_query_assets.append(clear_caracter_bruto_assets)
    except requests.exceptions.HTTPError:
        try:
            res_query_assets_3 = requests.get('https://' + k + '/api/open/query/do?' + query_assets,auth=HTTPBasicAuth(userr, pssword), verify=False)
            res_query_assets_3.raise_for_status()
            if res_query_assets_3.status_code == 200:
                    file_bruto_query_assets_3 = res_query_assets_3.text
                    texto_bruto_assets_3 = file_bruto_query_assets_3.split(",")
                    if texto_bruto_assets_3[-1] == '{"result":null':
                        list_query_assets.append('0')
                    else:
                        clear_texto_bruto_assets_3 = texto_bruto_assets_3[-1].replace('"total":', '')
                        clear_caracter_bruto_assets_3 = clear_texto_bruto_assets_3.replace('}', '')
                        list_query_assets.append(clear_caracter_bruto_assets_3)
        except requests.exceptions.HTTPError:
            list_query_assets.append(cadena_error)
        except requests.exceptions.ConnectionError:
            list_query_assets.append(cadena_error)
    except requests.exceptions.ConnectionError:
        list_query_assets.append(cadena_error)
    time.sleep(1)
    list_query_assets.append(time2)
    return list_query_assets


for k, v in list_sondas.items():
    query_conteo(k,v)
    query_nodes(k,v)
    query_assets(k,v)
    #print(list_query_assets)
    writer.writerow(list_query_assets)
    list_query_assets=[]

myFileCSV.close()

try:
    transport=paramiko.Transport((hostname, port))
    transport.connect(username=username,password=password)
    sftp=paramiko.SFTPClient.from_transport(transport)
    sftp.put(path_file_local,path_file_remote)
    sftp.close()
    transport.close()
    print(f"Transferencia SFTP exitosa: {path_file_local} -> {path_file_remote}")

except paramiko.AuthenticationException as auth_ex:
    print(f"Error de autenticacion: {auth_ex}")
except paramiko.SSHException as ssh_ex:
    print(f"Error de ssh: {ssh_ex}")
except paramiko.SFTPError as sftp_ex:
    print(f"Error de sftp: {sftp_ex}")
except IOError as io_ex:
    print(f"Error de E/S: {io_ex}")
except Exception as e:
    print(f"Error general: {e}")



