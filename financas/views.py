from django.shortcuts import render
import sqlite3
import pandas as pd 
from .models import Control
def index(request):
    
    df = pd.read_excel('C:\Git\Finantial_control\Controle_de_gastos_2023.xlsx')
    conn = sqlite3.connect('db.sqlite3')
    df.to_sql('financas_control', conn, if_exists='replace', index=False)
    conn.close()

    controls = Control.objects.filter()
    print(controls)
    return render(request, 'financas/index.html', {'controls':controls})