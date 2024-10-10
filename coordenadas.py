import pandas as pd
from geopy.distance import geodesic

clientes_df = pd.read_csv('1 - Clientes.csv')
fabricas_df = pd.read_csv('2 - Fabricas.csv', encoding='latin1')

print(clientes_df.head())

print(fabricas_df.head())

fabricas = [
    (fabricas_df['LAT'][0], fabricas_df['LONG'][0]),  # Fabrica Itu
    (fabricas_df['LAT'][1], fabricas_df['LONG'][1]),  # Fabrica Araraquara
    (fabricas_df['LAT'][2], fabricas_df['LONG'][2]),  # Fabrica Jacareí
]

for i, fabrica in enumerate(fabricas):
    for j, cliente in clientes_df.iterrows():
        cliente_coord = (cliente['LAT'], cliente['LONG'])
        distancia = geodesic(fabrica, cliente_coord).kilometers
        print(f"Fábrica {i + 1} x Cliente {j + 1} = {distancia:.2f} km")