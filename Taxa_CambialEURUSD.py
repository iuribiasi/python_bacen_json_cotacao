# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:29:19 2021

@author: Iuri Biasi
"""

import pandas as pd
import datetime
import numpy
from datetime import date, timedelta

data_atual = date.today()
data_15da = date.today() - timedelta(15)

USD_V = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json'
USD_C = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json'
EUR_V = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados?formato=json'
EUR_C = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21620/dados?formato=json'
IEN_V = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21621/dados?formato=json'
IEN_C = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21622/dados?formato=json'

"""
DOLAR PRICES
"""

df_usd_v = pd.read_json(USD_V)
df_usd_v.insert(1, 'moeda', 'USD Venda', allow_duplicates=True)

df_usd_c = pd.read_json(USD_C)
df_usd_c.insert(1, 'moeda', 'USD Compra', allow_duplicates=True)

"""
EUR PRICES
"""

df_eur_v = pd.read_json(EUR_V)
df_eur_v.insert(1, 'moeda', 'EUR Venda', allow_duplicates=True)

df_eur_c = pd.read_json(EUR_C)
df_eur_c.insert(1, 'moeda', 'EUR Compra', allow_duplicates=True)

"""
IEN PRICES
"""

df_ien_v = pd.read_json(IEN_V)
df_ien_v.insert(1, 'moeda', 'IEN Venda', allow_duplicates=True)

df_ien_c = pd.read_json(IEN_C)
df_ien_c.insert(1, 'moeda', 'IEN Compra', allow_duplicates=True)



"""
UNIR TODAS AS DFS NO RESULT E FILTRAR POR DATA, result é a DF completa, filtered_df é a DF Filtrada
"""

frames = [df_usd_v, df_usd_c, df_eur_v, df_eur_c, df_ien_v, df_ien_c]
result = pd.concat(frames)

result['data'] = pd.to_datetime(result['data'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

selecao = (result['data'] >= f'{data_15da}') & (result['data'] <= f'{data_atual}')
df_filtrado = result[selecao]

