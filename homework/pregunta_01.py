"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import glob
import os
import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    path = os.path.join("files/input", "clusters_report.txt")
    dataframe = pd.read_fwf(
        path,
        engine='python',
        skiprows=4,
        names=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    )
    
    # Normalize keywords: ensure single space between words, comma separated
    dataframe = dataframe.copy()
    dataframe['principales_palabras_clave'] = dataframe['principales_palabras_clave'].str.replace(r'\s+', ' ', regex=True).str.strip()
    columnas_fijas = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave']
    dataframe[columnas_fijas] = dataframe[columnas_fijas].ffill()
    dataframe = dataframe.groupby(columnas_fijas, as_index=False).agg({'principales_palabras_clave':' '.join})
    dataframe['porcentaje_de_palabras_clave'] = dataframe['porcentaje_de_palabras_clave'].apply(lambda x: str(x).replace(' %',''))
    dataframe['porcentaje_de_palabras_clave'] = dataframe['porcentaje_de_palabras_clave'].apply(lambda x: float(str(x).replace(',','.')))
    dataframe['cluster'] = dataframe['cluster'].apply(lambda x: int(float((str(x)))))
    dataframe['cantidad_de_palabras_clave'] = dataframe['cantidad_de_palabras_clave'].apply(lambda x: int(float((str(x)))))
    dataframe['principales_palabras_clave'] = dataframe['principales_palabras_clave'].apply(lambda x: str(x).replace('.',''))

    return dataframe

if __name__ == '__main__':
   print(pregunta_01())