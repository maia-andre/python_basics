import flet as ft
import datetime as dt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do SQLAlchemy para conexão com o MySQL
DATABASE_URL = "mysql+pymysql://root:xxxxxx@localhost/transporte"  # Ajuste conforme o seu MySQL
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
        ft.DataColumn(ft.Text("Selecionar")),
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

        # Salva no banco de dados
        nova_viagem = Viagem(
            nome=nome_solicitante,
            data=data_viagem,
            origem=origem,
            destino=destino,
            hora_saida=hora_saida,
            hora_retorno=hora_retorno,
            quantidade=quantidade,
            observacao=observacao,
            motorista="",
            veiculo="",
            status="Pendente"
        )
        session.add(nova_viagem)
        session.commit()

        # Adiciona a nova linha à tabela na interface
        linha = ft.DataRow(cells=[    
            ft.DataCell(ft.Checkbox()),  # Adiciona checkbox
            ft.DataCell(ft.Container(content=ft.Text(nome_solicitante, no_wrap=False), width=100)),
            ft.DataCell(ft.Container(content=ft.Text(data_viagem, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(origem, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text(destino, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text(hora_saida, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(hora_retorno, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(quantidade, no_wrap=False), width=50)),
            ft.DataCell(ft.Container(content=ft.Text(observacao, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text("", no_wrap=False), width=100)),
            ft.DataCell(ft.Container(content=ft.Text("", no_wrap=False), width=100)),
            ft.DataCell(ft.Container(content=ft.Text("Pendente", no_wrap=False), width=80))
        ])
        
        tabela.rows.append(linha)
        pagina.update()

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
            caixa_obs
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
        
        pagina.overlay.append(popup)  # Altera para usar overlay
        popup.open = True
        pagina.update()

    # Popup de senha para administrador
    def abrir_popup_admin(evento):
        # Cria o popup de senha
        senha_input = ft.TextField(label="Digite a senha", password=True)

        senha_popup = ft.AlertDialog(
            title=ft.Text("Acesso Administrativo"),
            content=ft.Column([
                senha_input,
            ]),
            actions=[
                ft.ElevatedButton("Confirmar", on_click=lambda e: validar_senha(senha_input, senha_popup))
            ]
        )
        
        pagina.overlay.append(senha_popup)  # Altera para usar overlay
        senha_popup.open = True
        pagina.update()

    # Validação da senha
    def validar_senha(senha_input, senha_popup):
        if senha_input.value == "sua_senha":  # Substitua "sua_senha" pela senha real
            # Atualiza a tabela para adicionar checkboxes
            for linha in tabela.rows:
                # Adiciona um checkbox em cada linha existente, se ainda não houver
                if len(linha.cells) < len(colunas):
                    linha.cells.insert(0, ft.DataCell(ft.Checkbox()))

            # Atualiza a tabela após adicionar os checkboxes
            tabela.update()

            # Adiciona linha de botões
            nova_linha = ft.Row([
                ft.ElevatedButton("Alterar Viagem"),
                ft.ElevatedButton("Duplicar Viagem"),
                ft.ElevatedButton("Excluir Viagem"),
            ], alignment="center")

            # Adiciona os botões logo abaixo da linha de botões de solicitar e admin
            pagina.add(nova_linha)  
            pagina.update()

        # Fecha o popup de senha
        senha_popup.open = False
        pagina.update()

    # Botão para admin
    botao_admin = ft.ElevatedButton("Modo Administrador", on_click=abrir_popup_admin)

    # 2 botões na mesma linha 
    botao_criar = ft.ElevatedButton("Criar Solicitação", on_click=abrir_popup)
    linha_botoes = ft.Row([botao_criar, botao_admin], alignment="center")
    
    # Adiciona os botões à página
    pagina.add(linha_botoes)

    # Carregar e adicionar as viagens à tabela
    viagens = carregar_viagens()
    for viagem in viagens:
        linha = ft.DataRow(cells=[
            ft.DataCell(ft.Checkbox()),  # Adiciona checkbox
            ft.DataCell(ft.Container(content=ft.Text(viagem.nome, no_wrap=False), width=100)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.data, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.origem, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.destino, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.hora_saida, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.hora_retorno, no_wrap=False), width=80)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.quantidade, no_wrap=False), width=50)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.observacao, no_wrap=False), width=150)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.motorista, no_wrap=False), width=100)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.veiculo, no_wrap=False), width=100)),
            ft.DataCell(ft.Container(content=ft.Text(viagem.status, no_wrap=False), width=80)),
        ])
        tabela.rows.append(linha)

    # Adiciona a tabela à página
    pagina.add(tabela)

    # Atualiza a página
    pagina.update()

# Inicializa o aplicativo Flet como um app web
ft.app(target=main)

 # Botão Admin 
    # irá abrir um modal que irá solicitar um código
    # a inserção do código irá permitir o admin alterar ou excluir viagens na última coluna
    

    

