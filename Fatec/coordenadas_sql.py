import pandas as pd
from geopy.distance import geodesic
from sqlalchemy import create_engine
from fpdf import FPDF

# Configuração da conexão com o banco de dados
engine = create_engine('sqlite:///seu_banco_de_dados.db')  # Ajuste para seu banco

# Consultar os dados
clientes_df = pd.read_sql('SELECT * FROM Clientes', engine)
fabricas_df = pd.read_sql('SELECT * FROM Fabricas', engine)

fabricas = [
    (fabricas_df['LAT'][0], fabricas_df['LONG'][0]),  # Fábrica Itu
    (fabricas_df['LAT'][1], fabricas_df['LONG'][1]),  # Fábrica Araraquara
    (fabricas_df['LAT'][2], fabricas_df['LONG'][2]),  # Fábrica Jacareí
]

# Criar um PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Adicionar título
pdf.cell(200, 10, txt="Distâncias entre Fábricas e Clientes", ln=True, align='C')

# Calcular e adicionar distâncias ao PDF
for i, fabrica in enumerate(fabricas):
    for j, cliente in clientes_df.iterrows():
        cliente_coord = (cliente['LAT'], cliente['LONG'])
        distancia = geodesic(fabrica, cliente_coord).kilometers
        resultado = f"Fábrica {i + 1} x Cliente {j + 1} = {distancia:.2f} km"
        print(resultado)  # Imprime no console
        pdf.cell(0, 10, txt=resultado, ln=True)

# Salvar o PDF
pdf.output("distancias.pdf")

print("PDF gerado com sucesso!")
