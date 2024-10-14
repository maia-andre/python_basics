import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

# Ler os arquivos CSV
clientes_df = pd.read_csv('fatec/1 - Clientes.csv')
fabricas_df = pd.read_csv('fatec/2 - Fabricas.csv', encoding='latin1')
rotas_df = pd.read_csv('fatec/3 - Rotas.csv')

# Renomear colunas dos DataFrames para garantir a padronização
clientes_df.rename(columns={
    'Cliente': 'CO_Cliente',
    'MUN': 'MUN',
    'LAT': 'LAT',
    'LON': 'LON' # LONG é um termo próprio no SQL - não deve ser usado para não gerar conflitos
}, inplace=True)

fabricas_df.rename(columns={
    'Fabrica': 'CO_Fabrica',
    'NO_MUN': 'NO_MUN',
    'NO_MUN_MIN': 'NO_MUN_MIN',
    'SG_UF': 'SG_UF',
    'LAT': 'LAT',
    'LONG': 'LON'  # LONG é um termo próprio no SQL - não deve ser usado para não gerar conflitos
}, inplace=True)

# Configuração da conexão com o banco de dados MySQL
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',  # substitua pelo seu usuário
    password='xxxxxx',  # substitua pela sua senha
    auth_plugin='mysql_native_password'
)

cursor = db_connection.cursor()

# Criar banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS fatec_api")
cursor.execute("USE fatec_api")

# Criar tabela Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    CO_Cliente INT,
    MUN VARCHAR(255),
    LAT FLOAT,
    LON FLOAT
)
""")

# Criar tabela Fabricas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Fabricas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    CO_Fabrica INT,
    NO_MUN VARCHAR(255),
    NO_MUN_MIN VARCHAR(255),
    SG_UF VARCHAR(10),
    LAT FLOAT,
    LON FLOAT
)
""")

# Criar tabela Rotas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Rotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Dt_Pedido DATE,
    Dt_Emissao DATE,
    Dt_Entrega DATE,
    Mes_Base INT,
    Ano_Exec INT,
    CO_Fabrica INT,
    CO_Cliente INT,
    Incoterm VARCHAR(255),
    Veiculo VARCHAR(255),
    Qtd_pallets INT,
    Qtd_Transp INT,
    Moeda VARCHAR(10),
    Vlr_Frete DECIMAL(10, 2)
)
""")

# Fechar a conexão do cursor
db_connection.commit()
cursor.close()

# Conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:xxxxxx@localhost/fatec_api')

# Inserir dados nas tabelas
clientes_df.to_sql('Clientes', con=engine, if_exists='append', index=False)
fabricas_df.to_sql('Fabricas', con=engine, if_exists='append', index=False)
rotas_df.to_sql('Rotas', con=engine, if_exists='append', index=False)

# Formatar datas para a tabela Rotas
rotas_df['Dt_Pedido'] = pd.to_datetime(rotas_df['Dt_Pedido'], format='%d/%m/%y')
rotas_df['Dt_Emissao'] = pd.to_datetime(rotas_df['Dt_Emissao'], format='%d/%m/%y')
rotas_df['Dt_Entrega'] = pd.to_datetime(rotas_df['Dt_Entrega'], format='%d/%m/%y')

print("Dados inseridos com sucesso!")

# Consultar os dados
clientes_df = pd.read_sql('SELECT * FROM Clientes', engine)
fabricas_df = pd.read_sql('SELECT * FROM Fabricas', engine)
rotas_df = pd.read_sql('SELECT * FROM Rotas', engine)

print("Consulta realizada com sucesso!")
