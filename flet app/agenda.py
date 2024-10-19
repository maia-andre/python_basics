import flet as ft

def main(pagina):
    # Título
    titulo = ft.Text("Secretaria da Educação - Agenda do Transporte", size=30, weight="bold")
    
    # Logo com ajuste de tamanho
    logo = ft.Image(src="flet app/logo.png", width=100, height=100)  # Ajuste os valores conforme necessário
    
    # Adicionando o logo à esquerda e o título ao lado
    row = ft.Row([logo, titulo], alignment="center")  # Centraliza a linha

    # Adicionando a linha à página
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
        
        # Cria a linha da tabela com os valores
        linha = ft.DataRow(cells=[
            ft.DataCell(ft.Text(nome_solicitante)),
            ft.DataCell(ft.Text(data_viagem)),
            ft.DataCell(ft.Text(origem)),
            ft.DataCell(ft.Text(destino)),
            ft.DataCell(ft.Text(hora_saida)),
            ft.DataCell(ft.Text(hora_retorno)),
            ft.DataCell(ft.Text(quantidade)),
            ft.DataCell(ft.Text(observacao)),
            ft.DataCell(ft.Text("")),  # Motorista (vazio por enquanto)
            ft.DataCell(ft.Text("")),  # Veículo (vazio por enquanto)
            ft.DataCell(ft.Text("Pendente"))  # Status inicial como "Pendente"
        ])
        
        # Adiciona a nova linha à tabela
        tabela.rows.append(linha)
        
        # Atualiza a tabela na página
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

    # Criando o popup
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
        
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # 2 botões na mesma linha 
    botao_criar = ft.ElevatedButton("Criar Solicitação", on_click=abrir_popup)
    botao_admin = ft.ElevatedButton("Modo Administrador")
    linha_botoes = ft.Row([botao_criar, botao_admin], alignment="center")
    
    # Adiciona a tabela e os botões à página
    pagina.add(linha_botoes)   
    pagina.add(tabela)


# Inicializa o aplicativo Flet como um app web
ft.app(target=main, view=ft.WEB_BROWSER)  # ou ft.WEB para rodar em um servidor


        # botão confirmar
            # insere as 8 informações na tabela
 # Botão Admin 
    # irá abrir um modal que irá solicitar um código
    # a inserção do código irá permitir o admin alterar ou excluir viagens na última coluna
    
#tabela - cabeçalho com 11 colunas
 # status
 # motorista
 # veículo
 # solicitante
 # data da viagem
 # origem
 # destino
 # hora de saída
 # retorno previsto
 # quantidade de passageiros
 # observações
 # 2 ícones - alterar e excluir
    # os ícones vão ser "clicáveis" apenas para o administrador

    

ft.app(main)