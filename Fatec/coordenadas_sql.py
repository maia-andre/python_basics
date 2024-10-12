import pandas as pd
from geopy.distance import geodesic
from sqlalchemy import create_engine
from fpdf import FPDF
import mysql.connector

# Configuração da conexão com o banco de dados MySQL
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',        # substitua pelo seu usuário
    password='071259Aa!',      # substitua pela sua senha
    auth_plugin='mysql_native_password'
)

cursor = db_connection.cursor()

# Criar banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS sua_base_de_dados")
cursor.execute("USE sua_base_de_dados")

# Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    LAT FLOAT,
    LON FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fabricas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    LAT FLOAT,
    LON FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Rotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origem VARCHAR(255),
    destino VARCHAR(255),
    distancia FLOAT
)
""")

# Fechar a conexão
db_connection.commit()
cursor.close()

# Conexão com o banco de dados usando SQLAlchemy para consultas
engine = create_engine('mysql+mysqlconnector://root:071259Aa!@localhost/sua_base_de_dados')

# Inserir dados de exemplo (caso não existam)
clientes_data = [
    (-23.456, -47.456),  # Cliente 1
    (-22.567, -48.567)   # Cliente 2
]

fabricas_data = [
    (-23.123, -47.123),  # Fábrica Itu
    (-22.123, -48.123),  # Fábrica Araraquara
    (-23.345, -45.678)   # Fábrica Jacareí
]

# Inserir dados nas tabelas
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',        # substitua pelo seu usuário
    password='071259Aa!',      # substitua pela sua senha
    auth_plugin='mysql_native_password',
    database='sua_base_de_dados'
)

for lat, lon in clientes_data:
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO Clientes (LAT, LON) VALUES (%s, %s)", (lat, lon))

for lat, lon in fabricas_data:
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO Fabricas (LAT, LON) VALUES (%s, %s)", (lat, lon))

db_connection.commit()
db_connection.close()

print("Dados inseridos com sucesso!")

# Consultar os dados
clientes_df = pd.read_sql('SELECT * FROM Clientes', engine)
fabricas_df = pd.read_sql('SELECT * FROM Fabricas', engine)

fabricas = [
    (fabricas_df['LAT'][0], fabricas_df['LON'][0]),  # Fábrica Itu
    (fabricas_df['LAT'][1], fabricas_df['LON'][1]),  # Fábrica Araraquara
    (fabricas_df['LAT'][2], fabricas_df['LON'][2]),  # Fábrica Jacareí
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
        cliente_coord = (cliente['LAT'], cliente['LON'])
        distancia = geodesic(fabrica, cliente_coord).kilometers
        resultado = f"Fábrica {i + 1} x Cliente {j + 1} = {distancia:.2f} km"
        print(resultado)  # Imprime no console
        pdf.cell(0, 10, txt=resultado, ln=True)

# Salvar o PDF
pdf.output("distancias.pdf")

print("PDF gerado com sucesso!")
