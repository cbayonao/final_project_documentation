#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import time

def scrap_law(process_id):
    """
    Method to scrape legal cases in Colombia
    """
    try:
        url = 'https://consultaprocesos.ramajudicial.gov.co/Procesos/NumeroRadicacion'
        """
        First get request
        """
        r = requests.get(url)
        t = 5
        time.sleep(t)
        s = BeautifulSoup(r.text, 'lxml')
        headers = r.headers
    except Exception as e:
        print("Error en el primer request:", e)
    try:
        """Parse first form to send in second post request"""
        formulario = s.find('form', attrs={'class':'consulta'}).find_all('input')
        for campo in formulario:
            form = {
                formulario[0].get('name'): formulario[0].get('value'),
                formulario[1].get('name'): formulario[1].get('value'),
                formulario[2].get('name'): formulario[2].get('value'),
                formulario[3].get('name'): formulario[3].get('value'),
                formulario[4].get('name'): formulario[4].get('value'),
                formulario[5].get('name'): formulario[5].get('value'),
                formulario[6].get('name'): process_id,
                formulario[7].get('name'): formulario[7].get('value')
            }
        """
        Second requests in this case POST
        """
        r = requests.post(url, form, headers)
        time.sleep(t)
        s = BeautifulSoup(r.text, 'lxml')
        headers = r.headers
        """Parse Second Form"""
        formulario = s.find('form', attrs={'class':'consulta'}).find_all('input')
        id_proc = s.find('a', attrs={'onclick':'PostIdProceso(event)'}).get('id')

        for campo in formulario:
            form = {
                formulario[0].get('name'): formulario[0].get('value'),
                formulario[1].get('name'): id_proc,
                formulario[2].get('name'): formulario[2].get('value'),
                formulario[3].get('name'): formulario[3].get('value'),
                formulario[4].get('name'): formulario[4].get('value'),
                formulario[5].get('name'): formulario[5].get('value'),
                formulario[6].get('name'): formulario[6].get('value'),
                formulario[7].get('name'): formulario[7].get('value')
            }
        newurl = r.request.url
    except Exception as e:
        print("Error en el segundo request: ", e)
    try:
        """
        This requests POST, finally get data_processes
        """
        r = requests.post(newurl, form, headers)
        time.sleep(t)
        s = BeautifulSoup(r.text, 'lxml')
    except Exception as e:
        print("Error en el tercer request: ", e)
    try:
        """
        Parse general data of the process_id
        """
        num_proc = s.find('span', attrs={'class': 'serial'}).text
        radicate_at = s.find('div', attrs={'id': 'FechaProceso'}).text.strip()
        TipoProceso = s.find('div', attrs={'id': 'TipoProceso'}).text.strip()
    except Exception as e:
        print("Error parseando la data general: ", e)
    try:
        """
        Parse parties data
        """
        tabla_partes = s.find_all('table')[2]
        table_rows = tabla_partes.find_all('tr')
        parties = {}
        for tr in table_rows:
            td = tr.find_all('td')
            for i in td:
                parties[td[2].text] = td[0].text
    except Exception as e:
        print("Error parseando la data de las partes: ", e)
    try:
        """
        Parse data of the judge by process_id
        """
        name_despacho = s.find('div', attrs={'id': 'Despacho'}).text.strip()
        judge = s.find('div', attrs={'id': 'Ponente'}).text.strip()
        county = name_despacho.split()[-1]
    except Exception as e:
        print("Error parseando la data del despacho: ", e)
    try:
        """
        Get key for data
        """
        title_table = s.find_all('table')[3].find('thead').find_all('th')[:-1]
        dic_actua = {}
        anotacion = 0
    except Exception as e:
        print('Error obteniendo la data:', e)
    try:
        """
        Parse data of the movements by process_id
        """
        tabla_movements = tabla_partes = s.find_all('table')[3]
        table_rows = tabla_movements.find_all('tr')
        for tr in table_rows:
            cont = 0
            new_anot = {}
            td = tr.find_all('td')
            for i in td:
                if cont < 6:
                    new_anot[title_table[cont].text.strip()] = i.text.strip()
                    cont += 1
            if new_anot:
                dic_actua[anotacion] = new_anot
            anotacion += 1
    except Exception as e:
        print("Error parseando la data de las actuaciones: ", e)
    try:
        """
        Unify information within a dictionary
        """
        data = {
            'process_id': num_proc,
            'radicate_at': radicate_at,
            'type_proc': TipoProceso,
            'parties': parties,
            'despacho': {
                'name': name_despacho,
                'judge': judge,
                'county': county
            },
            'movements': dic_actua,
            'location': county
        }
    except Exception as e:
        print("Error Unificando la data en el dictionary: ", e)
    try:
        """
        Convert it to JSON
        """
        with open("data_processes.json", 'w', encoding='utf8') as wf:
            json.dump(data, wf, ensure_ascii=False)
    except Exception as e:
        print("Error convirtiendo la data en json: ", e)

if __name__ == '__main__':
    scrap_law('11001221500020160010300')
