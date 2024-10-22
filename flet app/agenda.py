import flet as ft
import datetime as dt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do SQLAlchemy para conexão com o MySQL
DATABASE_URL = "mysql+pymysql://root:071259Aa!@localhost/transporte"  # Ajuste conforme o seu MySQL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Definir base do SQLAlchemy
Base = declarative_base()

# Definir modelo de dados para Viagem
class Viagem(Base):
    __tablename__ = 'viagens'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    data = Column(String(50))
    origem = Column(String(100))
    destino = Column(String(100))
    hora_saida = Column(String(50))
    hora_retorno = Column(String(50))
    quantidade = Column(Integer)
    observacao = Column(String(200))
    motorista = Column(String(100))
    veiculo = Column(String(100))
    status = Column(String(50))

# Cria as tabelas no banco de dados, caso ainda não existam
Base.metadata.create_all(engine)

def carregar_viagens():
    # Carregar viagens do banco de dados
    return session.query(Viagem).all()

def main(pagina):
    # Título
    titulo = ft.Text("Secretaria da Educação - Agenda do Transporte", size=30, weight="bold")
    
    # Logo com ajuste de tamanho
    logo = ft.Image(src="flet app/logo.png", width=100, height=100)
    
    # Adicionando o logo à esquerda e o título ao lado
    row = ft.Row([logo, titulo], alignment="center")
    pagina.add(row)

    # Criação da tabela
    colunas = [
        ft.DataColumn(ft.Text("Nome")),  
        ft.DataColumn(ft.Text("Data")),
        ft.DataColumn(ft.Text("Origem")),
        ft.DataColumn(ft.Text("Destino")),
        ft.DataColumn(ft.Text("Horário de Saída")),
        ft.DataColumn(ft.Text("Retorno Previsto")),
        ft.DataColumn(ft.Text("Passageiros")),
        ft.DataColumn(ft.Text("Obs")),
        ft.DataColumn(ft.Text("Motorista")),
        ft.DataColumn(ft.Text("Veículo")),
        ft.DataColumn(ft.Text("Status")),
    ]

    # Inicializa a tabela com as colunas e uma lista vazia de linhas
    tabela = ft.DataTable(columns=colunas, rows=[])

    # Usar ListView para adicionar barra de rolagem automática
    container_tabela = ft.ListView(
        controls=[tabela],
        auto_scroll=True,  # Rolar automaticamente
        expand=True,       # Faz a ListView expandir para preencher o espaço disponível
    )

    def salvar_viagem(evento):
        # Fecha o popup
        popup.open = False

        # Recupera os valores digitados pelo usuário
        nome_solicitante = caixa_nome.value
        data_viagem = caixa_data.value
        origem = caixa_origem.value
        destino = caixa_destino.value
        hora_saida = caixa_saida.value
        hora_retorno = caixa_retorno.value
        quantidade = caixa_qtde.value
        observacao = caixa_obs.value

        # Salva no banco de dados (sem motorista, veiculo, status)
        nova_viagem = Viagem(
            nome=nome_solicitante,
            data=data_viagem,
            origem=origem,
            destino=destino,
            hora_saida=hora_saida,
            hora_retorno=hora_retorno,
            quantidade=quantidade,
            observacao=observacao,
            motorista="",  # Definido diretamente na tabela
            veiculo="",    # Definido diretamente na tabela
            status="Pendente"  # Status inicial como Pendente
        )
        session.add(nova_viagem)
        session.commit()

        # Adiciona a nova linha à tabela na interface
        adicionar_linha_tabela(nova_viagem)

    def adicionar_linha_tabela(viagem):
        linha = ft.DataRow(cells=[
            ft.DataCell(ft.Container(content=ft.Text(viagem.nome, no_wrap=False), width=100)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.data, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.origem, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.destino, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.hora_saida, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.hora_retorno, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.quantidade, no_wrap=False), width=50)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.observacao, no_wrap=False), width=150)),
            
            # Dropdown para selecionar o motorista na própria tabela
            ft.DataCell(ft.Dropdown(
                value=viagem.motorista,
                options=[
                    ft.dropdown.Option("Airã"),
                    ft.dropdown.Option("Mauro"),
                    ft.dropdown.Option("Anderson"),
                    ft.dropdown.Option("Ulysses"),
                    ft.dropdown.Option("Ana Paula"),
                    ft.dropdown.Option("Ferreira"),
                    ft.dropdown.Option("Damasceno"),
                    ft.dropdown.Option("Rogério"),
                ],
                on_change=lambda e: atualizar_viagem_motorista(viagem.id, e.control.value)
            )),
            
            # Dropdown para selecionar o veículo na própria tabela
            ft.DataCell(ft.Dropdown(
                value=viagem.veiculo,
                options=[
                    ft.dropdown.Option("CRONOS"),
                    ft.dropdown.Option("C3"),
                    ft.dropdown.Option("ÔNIBUS"),
                    ft.dropdown.Option("MICRO"),
                    ft.dropdown.Option("VAN"),
                    ft.dropdown.Option("CAMINHÃO"),
                ],
                on_change=lambda e: atualizar_viagem_veiculo(viagem.id, e.control.value)
            )),
            
            # Dropdown para selecionar o status na própria tabela
            ft.DataCell(ft.Dropdown(
                value=viagem.status,
                options=[
                    ft.dropdown.Option("Pendente"),
                    ft.dropdown.Option("Aprovada"),
                    ft.dropdown.Option("Reprovado"),
                ],
                on_change=lambda e: atualizar_viagem_status(viagem.id, e.control.value)
            )),
        ])
        
        tabela.rows.append(linha)
        pagina.update()

    # Funções para atualizar os campos no banco de dados
    def atualizar_viagem_motorista(viagem_id, novo_motorista):
        viagem = session.query(Viagem).get(viagem_id)
        viagem.motorista = novo_motorista
        session.commit()

    def atualizar_viagem_veiculo(viagem_id, novo_veiculo):
        viagem = session.query(Viagem).get(viagem_id)
        viagem.veiculo = novo_veiculo
        session.commit()

    def atualizar_viagem_status(viagem_id, novo_status):
        viagem = session.query(Viagem).get(viagem_id)
        viagem.status = novo_status
        session.commit()

    # Criar solicitação
    titulo_popup = ft.Text("Solicite sua viagem!")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    caixa_data = ft.TextField(label="Digite a data da viagem")
    caixa_origem = ft.TextField(label="Digite a origem")
    caixa_destino = ft.TextField(label="Digite o destino")
    caixa_saida = ft.TextField(label="Digite o horário de saída")
    caixa_retorno = ft.TextField(label="Digite o horário de retorno")
    caixa_qtde = ft.TextField(label="Quantidade de passageiros")
    caixa_obs = ft.TextField(label="Observações")
    botao_solicitar = ft.ElevatedButton("Solicitar viagem!", on_click=salvar_viagem)

    # Criando o popup para solicitação
    popup = ft.AlertDialog(
        title=titulo_popup,
        content=ft.Column([
            caixa_nome,
            caixa_data,
            caixa_origem,
            caixa_destino,
            caixa_saida,
            caixa_retorno,
            caixa_qtde,
            caixa_obs,
        ]),
        actions=[botao_solicitar]
    )

    def abrir_popup(evento):
        # Limpa os campos antes de abrir o popup
        caixa_nome.value = ""
        caixa_data.value = ""
        caixa_origem.value = ""
        caixa_destino.value = ""
        caixa_saida.value = ""
        caixa_retorno.value = ""
        caixa_qtde.value = ""
        caixa_obs.value = ""
        
        pagina.overlay.append(popup)  # Adiciona o popup à overlay
        popup.open = True
        pagina.update()

    # Botão para criar solicitação
    botao_criar = ft.ElevatedButton("Criar Solicitação", on_click=abrir_popup)
    
    # Adiciona o botão à página
    pagina.add(botao_criar)

    # Carregar viagens do banco de dados e adicionar à tabela
    for viagem in carregar_viagens():
        adicionar_linha_tabela(viagem)

    # Adiciona o ListView da tabela à página
    pagina.add(container_tabela)

ft.app(target=main)

 # Botão Admin 
    # irá abrir um modal que irá solicitar um código
    # a inserção do código irá permitir o admin alterar ou excluir viagens na última coluna
    

    

