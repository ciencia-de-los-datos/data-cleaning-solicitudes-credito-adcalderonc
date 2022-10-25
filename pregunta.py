"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")


    df['sexo']=df.sexo.str.lower()
    df['tipo_de_emprendimiento']=df.tipo_de_emprendimiento.str.lower()
    df['idea_negocio']=df.idea_negocio.str.lower().str.replace(' ', '_').str.replace('-', '_')
    df['barrio']=df.barrio.str.lower().str.replace(' ', '_').str.replace('-', '_').str.replace('.', '')
    df['monto_del_credito']=df.monto_del_credito.str.replace('$', '').str.replace(',', '')
    df['monto_del_credito']=df.monto_del_credito.map(lambda x: x.replace('.00', '') if re.search(r".\d{2}$", x) else x)
    df['línea_credito']=df.línea_credito.str.lower().str.replace(' ', '_').str.replace('-', '_')

    df.dropna(subset=['sexo'], inplace= True)
    df.dropna(subset=['tipo_de_emprendimiento'], inplace= True)
    df.dropna(subset=['idea_negocio'], inplace= True)
    df.dropna(subset=['barrio'], inplace= True)
    df.dropna(subset=['monto_del_credito'], inplace= True)
    df.dropna(subset=['línea_credito'], inplace= True)
    

    return df
