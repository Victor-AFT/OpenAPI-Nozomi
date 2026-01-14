# date_creation: 10/01/2024
# Author: Victor Fuentes Toledo
# Version: 1.0

import paramiko
import requests
import urllib3
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os
import time
import csv


list_querys=[]
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

path_file_local='Output/Nozomi_nodos_enlaces.csv'
path_file_remote='/opt/kpi-nozomi-logstash/Nozomi_nodos_enlaces.csv'


myFileCSV=open(path_file_local,'w',encoding='utf-8', newline='')
writer=csv.writer(myFileCSV)

'USUARIO NOZOMI'
userr='nozomi'
pssword='nozomi'

'Nodos aprendidos (True y False)'
def query_nodos_aprendidos(k,v):
    query_nodos_aprendidos = 'query=nodes | group_by is_learned | sort is_learned | select is_learned count'
    try:
        res_query_nodos_aprendidos = requests.get('https://' + k + '/api/open/query/do?' + query_nodos_aprendidos,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_nodos_aprendidos.raise_for_status()
        if res_query_nodos_aprendidos.status_code==200:
                file_bruto_query_nodos_aprendidos = res_query_nodos_aprendidos.text
                texto_nodos_aprendidos= file_bruto_query_nodos_aprendidos.split(",")
                #print(texto_nodos_aprendidos[:4])

                'is_learned:false'
                islearnedfalse_bruto=texto_nodos_aprendidos[1].split(":")[1]
                format_islearnedfalse = islearnedfalse_bruto.replace('"', '')
                islearnedfalse = format_islearnedfalse.replace('}', '')

                'is_learned:true'
                islearnedtrue_bruto=texto_nodos_aprendidos[3].split(":")[1]
                format_islearnedtrue=islearnedtrue_bruto.replace('"','')
                format_islearnedtrue02=format_islearnedtrue.replace('}','')
                islearnedtrue=format_islearnedtrue02.replace(']','')

                #print("is_learned:false -> %s is_learned:true-> %s" % (islearnedfalse, islearnedtrue))

                list_querys.append(k)
                list_querys.append(v)
                list_querys.append(islearnedtrue)
                list_querys.append(islearnedfalse)


    except requests.exceptions.HTTPError:
        try:
            res_query_nodos_aprendidos_02 = requests.get('https://' + k + '/api/open/query/do?' + query_nodos_aprendidos,auth=HTTPBasicAuth(userr, pssword), verify=False)
            res_query_nodos_aprendidos_02.raise_for_status()
            if res_query_nodos_aprendidos_02.status_code == 200:
                file_bruto_query_nodos_aprendidos_02 = res_query_nodos_aprendidos_02.text
                texto_nodos_aprendidos_02 = file_bruto_query_nodos_aprendidos_02.split(",")
                # print(texto_nodos_aprendidos[:4])

                'is_learned:false'
                islearnedfalse_bruto_02 = texto_nodos_aprendidos_02[1].split(":")[1]
                format_islearnedfalse_02 = islearnedfalse_bruto_02.replace('"', '')
                islearnedfalse_02 = format_islearnedfalse_02.replace('}', '')

                'is_learned:true'
                islearnedtrue_bruto_02 = texto_nodos_aprendidos_02[3].split(":")[1]
                format_islearnedtrue_02 = islearnedtrue_bruto_02.replace('"', '')
                format_islearnedtrue02_02 = format_islearnedtrue_02.replace('}', '')
                islearnedtrue_02 = format_islearnedtrue02_02.replace(']', '')

                # print("is_learned:false -> %s is_learned:true-> %s" % (islearnedfalse_02, islearnedtrue_02))

                list_querys.append(k)
                list_querys.append(v)
                list_querys.append(islearnedtrue_02)
                list_querys.append(islearnedfalse_02)


        except requests.exceptions.HTTPError:
            list_querys.append(k)
            list_querys.append(v)
            list_querys.append(cadena_error)
        except requests.exceptions.ConnectionError:
            list_querys.append(k)
            list_querys.append(v)
            list_querys.append(cadena_error)

    except requests.exceptions.ConnectionError:
        list_querys.append(k)
        list_querys.append(v)
        list_querys.append(cadena_error)
    time.sleep(1)
    return list_querys

'Nodos NO completamente aprendidos'
def query_nodos_no_completamente_aprendidos(k,v):
    query_nodos_no_completamente_aprendidos = 'query=nodes | where is_learned == true and  is_fully_learned == false  | count'
    try:
        res_query_nodos = requests.get('https://' + k + '/api/open/query/do?' + query_nodos_no_completamente_aprendidos,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_nodos.raise_for_status()
        if res_query_nodos.status_code==200:
            file_bruto_query_nodes = res_query_nodos.text
            texto_bruto = file_bruto_query_nodes.split(",")
            format_textobruto=texto_bruto[0].split(":")[2].replace('"','')
            format_textobruto01=format_textobruto.replace("}","")
            no_completamente_aprendidos=format_textobruto01.replace("]","")
            list_querys.append(no_completamente_aprendidos)
    except requests.exceptions.HTTPError:
        try:
            res_query_nodos_02 = requests.get('https://' + k + '/api/open/query/do?' + query_nodos_no_completamente_aprendidos,
                auth=HTTPBasicAuth(userr, pssword), verify=False)
            res_query_nodos_02.raise_for_status()
            if res_query_nodos_02.status_code == 200:
                file_bruto_query_nodes_02 = res_query_nodos_02.text
                texto_bruto_02 = file_bruto_query_nodes_02.split(",")
                format_textobruto_02 = texto_bruto_02[0].split(":")[2].replace('"', '')
                format_textobruto01_02 = format_textobruto_02.replace("}", "")
                no_completamente_aprendidos_02 = format_textobruto01_02.replace("]", "")
                list_querys.append(no_completamente_aprendidos_02)
        except requests.exceptions.HTTPError:
            list_querys.append(cadena_error)
        except requests.exceptions.ConnectionError:
            list_querys.append(cadena_error)
    except requests.exceptions.ConnectionError:
        list_querys.append(cadena_error)
    time.sleep(1)
    return list_querys

'Links NO completamente aprendidos'
def query_enlaces_no_completamente_aprendidos(k,v):
    query_enlaces = 'query=links | where is_learned == true  and is_fully_learned == false  | count'
    try:
        res_query_enlaces = requests.get('https://' + k + '/api/open/query/do?' + query_enlaces,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_enlaces.raise_for_status()
        if res_query_enlaces.status_code == 200:
            file_bruto_query_nodes = res_query_enlaces.text
            texto_bruto = file_bruto_query_nodes.split(",")
            format_textobruto = texto_bruto[0].split(":")[2].replace('"', '')
            format_textobruto01 = format_textobruto.replace("}", "")
            no_completamente_aprendidos_enlaces = format_textobruto01.replace("]", "")
            list_querys.append(no_completamente_aprendidos_enlaces)
    except requests.exceptions.HTTPError:
        try:
            res_query_enlaces_02 = requests.get(
                'https://' + k + '/api/open/query/do?' + query_enlaces,auth=HTTPBasicAuth(userr, pssword), verify=False)
            res_query_enlaces_02.raise_for_status()
            if res_query_enlaces_02.status_code == 200:
                file_bruto_query_nodes_02 = res_query_enlaces_02.text
                texto_bruto_02 = file_bruto_query_nodes_02.split(",")
                format_textobruto_02 = texto_bruto_02[0].split(":")[2].replace('"', '')
                format_textobruto01_02 = format_textobruto_02.replace("}", "")
                no_completamente_aprendidos_enlaces_02 = format_textobruto01_02.replace("]", "")
                list_querys.append(no_completamente_aprendidos_enlaces_02)
        except requests.exceptions.HTTPError:
            list_querys.append(cadena_error)
        except requests.exceptions.ConnectionError:
            list_querys.append(cadena_error)
    except requests.exceptions.ConnectionError:
        list_querys.append(cadena_error)
    time.sleep(1)
    return list_querys

'links aprendidos (True y False)'
def query_enlaces_aprendidos(k,v):
    query_links_aprendidos = 'query=links | group_by is_learned | sort is_learned | select is_learned count'
    try:
        res_query_links_aprendidos = requests.get('https://' + k + '/api/open/query/do?' + query_links_aprendidos,auth=HTTPBasicAuth(userr, pssword), verify=False)
        res_query_links_aprendidos.raise_for_status()
        if res_query_links_aprendidos.status_code==200:
                file_bruto_query_links_aprendidos = res_query_links_aprendidos.text
                texto_links_aprendidos= file_bruto_query_links_aprendidos.split(",")
                #print(texto_nodos_aprendidos[:4])

                'is_learned:false'
                islearnedfalse_bruto=texto_links_aprendidos[1].split(":")[1]
                format_islearnedfalse = islearnedfalse_bruto.replace('"', '')
                islearnedfalse = format_islearnedfalse.replace('}', '')

                'is_learned:true'
                islearnedtrue_bruto=texto_links_aprendidos[3].split(":")[1]
                format_islearnedtrue=islearnedtrue_bruto.replace('"','')
                format_islearnedtrue02=format_islearnedtrue.replace('}','')
                islearnedtrue=format_islearnedtrue02.replace(']','')

                #print("is_learned:false -> %s is_learned:true-> %s" % (islearnedfalse, islearnedtrue))

                #list_querys.append(k)
                #list_querys.append(v)
                list_querys.append(islearnedtrue)
                list_querys.append(islearnedfalse)


    except requests.exceptions.HTTPError:
        try:
            res_query_links_aprendidos_02 = requests.get('https://' + k + '/api/open/query/do?' + query_links_aprendidos,auth=HTTPBasicAuth(userr, pssword), verify=False)
            res_query_links_aprendidos_02.raise_for_status()
            if res_query_links_aprendidos_02.status_code == 200:
                file_bruto_query_links_aprendidos_02 = res_query_links_aprendidos_02.text
                texto_links_aprendidos_02 = file_bruto_query_links_aprendidos_02.split(",")

                'is_learned:false'
                islearnedfalse_bruto_02 = texto_links_aprendidos_02[1].split(":")[1]
                format_islearnedfalse_02 = islearnedfalse_bruto_02.replace('"', '')
                islearnedfalse_02 = format_islearnedfalse_02.replace('}', '')

                'is_learned:true'
                islearnedtrue_bruto_02 = texto_links_aprendidos_02[3].split(":")[1]
                format_islearnedtrue_02 = islearnedtrue_bruto_02.replace('"', '')
                format_islearnedtrue02_02 = format_islearnedtrue_02.replace('}', '')
                islearnedtrue_02 = format_islearnedtrue02_02.replace(']', '')

                # print("is_learned:false -> %s is_learned:true-> %s" % (islearnedfalse_02, islearnedtrue_02))

                #list_querys.append(k)
                #list_querys.append(v)
                list_querys.append(islearnedtrue_02)
                list_querys.append(islearnedfalse_02)


        except requests.exceptions.HTTPError:
            list_querys.append(k)
            list_querys.append(v)
            list_querys.append(cadena_error)
        except requests.exceptions.ConnectionError:
            list_querys.append(k)
            list_querys.append(v)
            list_querys.append(cadena_error)

    except requests.exceptions.ConnectionError:
        list_querys.append(k)
        list_querys.append(v)
        list_querys.append(cadena_error)
    time.sleep(1)
    return list_querys


ordena_list_querys=[]
#['10.199.97.154', 'Guadame', '2813', '2502', '0', '7172', '400', '0']
for k, v in list_sondas.items():
    query_nodos_aprendidos(k,v)
    query_nodos_no_completamente_aprendidos(k,v)
    query_enlaces_aprendidos(k, v)
    query_enlaces_no_completamente_aprendidos(k, v)

    ordena_list_querys.append(list_querys[0])
    ordena_list_querys.append(list_querys[1])
    ordena_list_querys.append(list_querys[2])
    ordena_list_querys.append(list_querys[4])
    ordena_list_querys.append(list_querys[3])
    ordena_list_querys.append(list_querys[5])
    ordena_list_querys.append(list_querys[7])
    ordena_list_querys.append(list_querys[6])

    writer.writerow(ordena_list_querys)
    list_querys=[]
    ordena_list_querys = []

myFileCSV.close()

time.sleep(5)
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


