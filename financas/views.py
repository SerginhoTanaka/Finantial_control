from django.shortcuts import render
import json
import sqlite3
import pandas as pd 

def index(request):
    
    df = pd.read_excel('C:\Git\Controle-financeiro\Controle_de_gastos_2023.xlsx')
    df = df.iloc[7:23, :7]
    conn = sqlite3.connect('db.sqlite3')
    df.to_sql('financas_control', conn, if_exists='replace', index=False)
    conn.close()
    return render(request, 'financas/index.html')

def export_xls(request):

    return