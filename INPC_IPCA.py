# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:29:19 2021

@author: I7770871
"""


from bs4 import BeautifulSoup
import pandas as pd
import requests

"""
PEGANDO IPCA
"""
req = requests.get('https://www.idinheiro.com.br/tabelas/tabela-ipca/')
content = req.content
soup = BeautifulSoup(content, 'html.parser')
tabela = soup.find(name='table')
table_str = str(tabela)
df = pd.read_html(table_str)[0]
df.loc[:, 'Variação em %'] = df['Variação em %'] / 10000
df.loc[:, 'Variação no Ano'] = df['Variação no Ano'] / 10000
df.loc[:, 'Acumulado 12 meses'] = df['Acumulado 12 meses'] / 10000
df.rename(columns={'Variação em %': 'IPCA', 'Variação no Ano': 'IPCAYTD', 'Acumulado 12 meses': 'IPCA12M'}, inplace=True)


"""
PEGANDO INPC
"""
req2 = requests.get('https://www.idinheiro.com.br/tabelas/tabela-inpc/')
content2 = req2.content
soup2 = BeautifulSoup(content2, 'html.parser')
tabela2 = soup2.find(name='table')
table_str2 = str(tabela2)
df2 = pd.read_html(table_str2)[0]
df2.loc[:, 'Variação em %'] = df2['Variação em %'] / 10000
df2.loc[:, 'Variação no Ano'] = df2['Variação no Ano'] / 10000
df2.loc[:, 'Acumulado 12 meses'] = df2['Acumulado 12 meses'] / 10000
df2.rename(columns={'Variação em %': 'INPC', 'Variação no Ano': 'INPCYTD', 'Acumulado 12 meses': 'INPC12M'}, inplace=True)


"""
FAZENDO O MERGE E SALVANDO NA PASTA
"""

df3 = pd.merge(df, df2, how = 'outer')
print(df3)
df3.to_excel('//Qsbrprd/qliksense/BRASIL/OUTRAS FONTES/PCR_INDUSTRIAL/Finance/ÍNDICES/INFLAÇÃO.xlsx', index = False)
