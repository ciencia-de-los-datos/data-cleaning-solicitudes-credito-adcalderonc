"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    def format_date(str_date):
        d = re.search(r'(^\d+)\/(\d+)\/(\d+)', str_date, re.IGNORECASE)
        day = d.group(1)
        month = d.group(2)
        year = d.group(3)
        if len(day)>2:
            date = year + '/' + month + '/' + day
            return date
        else:
            date = day + '/' + month + '/' + year
            return date
    df4=df4[df4.columns[1:]]
    df['fecha_de_beneficio']=df.fecha_de_beneficio.apply(format_date)

    df['sexo']=df.sexo.str.lower()
    df['tipo_de_emprendimiento']=df.tipo_de_emprendimiento.str.lower()
    df['idea_negocio']=df.idea_negocio.str.lower().str.replace(' ', '_').str.replace('-', '_')
    df['barrio']=df.barrio.str.lower().str.replace(' ', '_').str.replace('-', '_').str.replace('.', '')
    df['monto_del_credito']=df.monto_del_credito.str.replace('$', '').str.replace(',', '')
    df['monto_del_credito']=df.monto_del_credito.map(lambda x: float(x))
    df['línea_credito']=df.línea_credito.str.lower().str.replace('_', ' ').str.replace('-', ' ')

    df.dropna(inplace= True)
    df.drop_duplicates(inplace= True)
 

    return df
